from pathlib import Path

def safe_filename(name: str) -> str:
    return "".join(c for c in name if c.isalnum() or c in "-_ ").strip().replace(" ", "_")
