def truncate(text: str, length: int = 160) -> str:
    return text if len(text) <= length else text[:length-1] + "…"
