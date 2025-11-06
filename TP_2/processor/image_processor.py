
from PIL import Image
import io
from common.serialization import b64encode
import requests

def _download_image(url: str, timeout=10):
    try:
        r = requests.get(url, timeout=timeout, stream=True)
        r.raise_for_status()
        return r.content[:2_000_000]
    except Exception:
        return None

def thumbnails_from_links(links, max_thumbs=3, size=(200, 200)):
    thumbs = []
    for href in links:
        if len(thumbs) >= max_thumbs:
            break
        if not any(href.lower().endswith(ext) for ext in (".png", ".jpg", ".jpeg", ".gif", ".webp")):
            continue
        raw = _download_image(href)
        if not raw:
            continue
        try:
            im = Image.open(io.BytesIO(raw))
            im.thumbnail(size)
            out = io.BytesIO()
            im.save(out, format="PNG")
            thumbs.append(b64encode(out.getvalue()))
        except Exception:
            continue
    return thumbs
