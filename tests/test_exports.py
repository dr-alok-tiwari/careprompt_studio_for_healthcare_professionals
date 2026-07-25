from services.export_service import as_markdown, as_docx, as_pdf

def test_exports_nonempty():
    assert "Title" in as_markdown("Title","Body")
    assert len(as_docx("Title","Body")) > 10
    assert len(as_pdf("Title","Body")) > 10
