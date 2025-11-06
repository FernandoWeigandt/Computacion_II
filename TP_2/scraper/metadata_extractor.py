
def extract_meta(scraping_result: dict) -> dict:
    # Hook para futuras ampliaciones (JSON-LD, Schema.org, etc.).
    return scraping_result.get("meta_tags", {})
