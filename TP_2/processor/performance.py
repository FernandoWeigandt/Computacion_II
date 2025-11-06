
def analyze_performance(main_elapsed_s: float, headers: dict, num_links: int, images_count: int) -> dict:
    num_requests = 1 + min(60, images_count // 2 + num_links // 20)
    total_size_kb = 0.0
    cl = headers.get("Content-Length") or headers.get("content-length")
    try:
        if cl:
            total_size_kb += int(cl) / 1024.0
    except Exception:
        pass
    total_size_kb += images_count * 12.5 + (num_links // 10) * 4.0
    load_time_ms = int(max(1e-3, main_elapsed_s) * 1000)
    return {
        "load_time_ms": load_time_ms,
        "total_size_kb": int(total_size_kb),
        "num_requests": int(num_requests),
    }
