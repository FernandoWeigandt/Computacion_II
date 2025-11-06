
#!/usr/bin/env python3
import argparse, asyncio, socket
from aiohttp import web
from scraper.async_http import AsyncHTTPClient
from scraper.html_parser import parse_basic
from scraper.metadata_extractor import extract_meta
from common.protocol import pack_message, recv_message
from datetime import datetime, timezone

def _is_ipv6(addr: str) -> bool:
    return ":" in addr

async def scrape_and_process(url: str, proc_host: str, proc_port: int):
    async with AsyncHTTPClient(max_conn_per_host=10) as http:
        html, headers, status, elapsed = await http.get_text(url)
    if status >= 400:
        raise web.HTTPBadRequest(text=f"Fetch failed with status {status}")

    parsed = parse_basic(url, html)
    meta = extract_meta(parsed)

    job = {
        "url": url,
        "title": parsed.get("title",""),
        "main_elapsed_s": elapsed,
        "headers": headers,
        "links": parsed.get("links", []),
        "images_count": parsed.get("images_count", 0),
    }

    def _talk_with_processing(job):
        family = socket.AF_INET6 if _is_ipv6(proc_host) else socket.AF_INET
        with socket.socket(family, socket.SOCK_STREAM) as s:
            s.settimeout(20)
            s.connect((proc_host, proc_port))
            s.sendall(pack_message(job))
            return recv_message(s)

    resp = await asyncio.to_thread(_talk_with_processing, job)
    if not resp.get("ok"):
        raise web.HTTPBadGateway(text=f"processing error: {resp.get('error')}")
    processing_data = resp["result"]

    now = datetime.now(timezone.utc).isoformat()
    return {
        "url": url,
        "timestamp": now,
        "scraping_data": {
            "title": parsed["title"],
            "links": parsed["links"],
            "meta_tags": meta,
            "structure": parsed["structure"],
            "images_count": parsed["images_count"],
        },
        "processing_data": processing_data,
        "status": "success",
    }

async def handle_scrape(request: web.Request):
    url = request.query.get("url")
    if not url:
        raise web.HTTPBadRequest(text="missing ?url=")
    try:
        result = await scrape_and_process(
            url,
            request.app["proc_host"],
            request.app["proc_port"],
        )
        return web.json_response(result)
    except asyncio.TimeoutError:
        raise web.HTTPGatewayTimeout(text="timeout")
    except Exception as e:
        return web.json_response({"status":"error","error":str(e)}, status=502)

def make_app(proc_host: str, proc_port: int) -> web.Application:
    app = web.Application()
    app["proc_host"] = proc_host
    app["proc_port"] = proc_port
    app.router.add_get("/scrape", handle_scrape)
    return app

def main():
    ap = argparse.ArgumentParser(description="Servidor de Scraping Web Asíncrono")
    ap.add_argument("-i", "--ip", required=True, help="Dirección de escucha (IPv4/IPv6)")
    ap.add_argument("-p", "--port", required=True, type=int, help="Puerto de escucha")
    ap.add_argument("-w", "--workers", type=int, default=4, help="Workers HTTP (aiohttp)")
    ap.add_argument("--proc-host", required=True, help="Host del servidor de procesamiento (IPv4/IPv6)")
    ap.add_argument("--proc-port", required=True, type=int, help="Puerto del servidor de procesamiento")
    args = ap.parse_args()

    app = make_app(args.proc_host, args.proc_port)
    web.run_app(app, host=args.ip, port=args.port)

if __name__ == "__main__":
    main()
