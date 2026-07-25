from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def load_json(name: str):
    with open(ROOT / "data" / name, encoding="utf-8") as f:
        return json.load(f)
