import json
from pathlib import Path

def test_templates_valid():
    p=Path(__file__).resolve().parents[1]/"data"/"prompt_templates.json"
    data=json.loads(p.read_text())
    assert len(data) >= 150
    assert all("prompt_template" in x for x in data)
