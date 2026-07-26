from itertools import product

from services.tool_registry import filter_tools, load_tools


def test_tools_load():
    df = load_tools()
    assert len(df) >= 75
    assert {
        "tool",
        "category",
        "access",
        "cost_inr",
        "official_url",
    }.issubset(df.columns)
    assert df["cost_inr"].str.contains("₹", regex=False).all()
    assert df["official_url"].str.startswith(("https://", "http://")).all()


def test_filter():
    assert len(filter_tools("Zotero")) == 1


def test_every_category_access_combination_has_a_tool():
    df = load_tools()
    for category, access in product(
        sorted(df["category"].unique()),
        sorted(df["access"].unique()),
    ):
        assert not filter_tools(category=category, access=access).empty, (
            f"No tool for category={category!r}, access={access!r}"
        )
