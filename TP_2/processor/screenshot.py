
from PIL import Image, ImageDraw, ImageFont
import io
from common.serialization import b64encode

def render_placeholder_screenshot(url: str, title: str) -> str:
    img = Image.new("RGB", (960, 540), (240, 240, 255))
    draw = ImageDraw.Draw(img)
    text = (title or "Sin título")[:80]
    url_line = (url or "")[:80]
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None
    draw.text((30, 40), "Screenshot (placeholder)", fill=(20, 20, 20), font=font)
    draw.text((30, 120), f"Title: {text}", fill=(20, 20, 20), font=font)
    draw.text((30, 160), f"URL: {url_line}", fill=(20, 20, 20), font=font)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return b64encode(buf.getvalue())
