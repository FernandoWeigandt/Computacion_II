
#!/usr/bin/env python3
import argparse, socket, socketserver, os, multiprocessing
from concurrent.futures import ProcessPoolExecutor
from common.protocol import recv_message, pack_message
from processor.screenshot import render_placeholder_screenshot
from processor.performance import analyze_performance
from processor.image_processor import thumbnails_from_links

def _is_ipv6(addr: str) -> bool:
    return ":" in addr

def _process_job(job: dict) -> dict:
    url = job.get("url","")
    title = job.get("title","")
    perf = analyze_performance(job.get("main_elapsed_s", 1.0), job.get("headers", {}), len(job.get("links", [])), job.get("images_count", 0))
    screenshot = render_placeholder_screenshot(url, title)
    thumbs = thumbnails_from_links(job.get("links", []), max_thumbs=3)
    return {
        "screenshot": screenshot,
        "performance": perf,
        "thumbnails": thumbs,
    }

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            job = recv_message(self.request)
            # Enviar al pool (el ejecutor se guarda en server.executor)
            result = self.server.executor.submit(_process_job, job).result()
            self.request.sendall(pack_message({"ok": True, "result": result}))
        except Exception as e:
            try:
                self.request.sendall(pack_message({"ok": False, "error": str(e)}))
            except Exception:
                pass

def main():
    ap = argparse.ArgumentParser(description="Servidor de Procesamiento Distribuido")
    ap.add_argument("-i", "--ip", required=True, help="Dirección de escucha (IPv4/IPv6)")
    ap.add_argument("-p", "--port", required=True, type=int, help="Puerto de escucha")
    ap.add_argument("-n", "--processes", type=int, default=0, help="Número de procesos (default: CPU count)")
    args = ap.parse_args()

    procs = args.processes if args.processes and args.processes > 0 else (os.cpu_count() or 2)

    class V6Server(socketserver.TCPServer):
        address_family = socket.AF_INET6
        allow_reuse_address = True

    class V4Server(socketserver.TCPServer):
        address_family = socket.AF_INET
        allow_reuse_address = True

    ServerCls = V6Server if _is_ipv6(args.ip) else V4Server
    with ServerCls((args.ip, args.port), Handler) as server:
        server.executor = ProcessPoolExecutor(max_workers=procs, mp_context=multiprocessing.get_context("spawn"))
        print(f"[processing] listening on {args.ip}:{args.port} with {procs} processes")
        try:
            server.serve_forever()
        finally:
            server.executor.shutdown(wait=True, cancel_futures=True)

if __name__ == "__main__":
    main()
