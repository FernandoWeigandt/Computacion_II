
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parse_basic(url: str, html: str):
    soup = BeautifulSoup(html, "lxml")

    title = (soup.title.string.strip() if soup.title and soup.title.string else "")

    links = []
    for a in soup.find_all("a", href=True):
        links.append(urljoin(url, a["href"]))

    meta = {}
    for tag in soup.find_all("meta"):
        name = (tag.get("name") or tag.get("property") or "").lower()
        if not name:
            continue
        if name in {"description", "keywords"} or name.startswith("og:"):
            meta[name] = tag.get("content", "")

    headers = {}
    for level in range(1, 7):
        headers[f"h{level}"] = len(soup.find_all(f"h{level}"))

    images_count = len(soup.find_all("img"))
    return {
        "title": title,
        "links": links,
        "meta_tags": meta,
        "structure": headers,
        "images_count": images_count,
    }
