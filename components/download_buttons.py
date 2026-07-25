import streamlit as st
from services.export_service import as_docx, as_pdf

def document_downloads(title: str, content: str, key: str) -> None:
    c1, c2 = st.columns(2)
    c1.download_button("DOCX", as_docx(title, content), f"{key}.docx", key=f"{key}_docx")
    c2.download_button("PDF", as_pdf(title, content), f"{key}.pdf", key=f"{key}_pdf")
