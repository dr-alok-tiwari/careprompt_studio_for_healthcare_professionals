from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "tool_directory.csv"

def load_tools() -> pd.DataFrame:
    return pd.read_csv(DATA).fillna("")


def filter_tools(query: str = "", category: str = "All", access: str = "All") -> pd.DataFrame:
    df = load_tools()
    if category != "All":
        df = df[df["category"] == category]
    if access != "All":
        df = df[df["access"] == access]
    if query:
        q = query.lower()
        mask = df.astype(str).apply(lambda col: col.str.lower().str.contains(q, regex=False)).any(axis=1)
        df = df[mask]
    return df.reset_index(drop=True)
