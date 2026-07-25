from pathlib import Path
import json
import pandas as pd


def validate_project_data(root: Path) -> list[str]:
    errors: list[str] = []
    templates = root / "data" / "prompt_templates.json"
    tools = root / "data" / "tool_directory.csv"
    try:
        data = json.loads(templates.read_text(encoding="utf-8"))
        if len(data) < 150:
            errors.append("Prompt library contains fewer than 150 templates.")
    except Exception as exc:
        errors.append(f"Prompt template error: {exc}")
    try:
        frame = pd.read_csv(tools)
        required = {"tool", "category", "access", "patient_data", "official_url"}
        if not required.issubset(frame.columns):
            errors.append("Tool directory is missing required columns.")
    except Exception as exc:
        errors.append(f"Tool directory error: {exc}")
    return errors
