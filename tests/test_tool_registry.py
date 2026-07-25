from services.tool_registry import load_tools, filter_tools

def test_tools_load():
    df=load_tools(); assert len(df) >= 50; assert "tool" in df.columns

def test_filter():
    assert len(filter_tools("Zotero")) == 1
