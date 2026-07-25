import html
import streamlit.components.v1 as components


def copy_button(text: str, label: str = "Copy prompt", height: int = 50) -> None:
    escaped = html.escape(text).replace("\n", "&#10;")
    components.html(
        f"""
        <textarea id="cptext" style="position:absolute;left:-9999px;">{escaped}</textarea>
        <button onclick="navigator.clipboard.writeText(document.getElementById('cptext').value); this.innerText='Copied ✓';"
        style="min-height:42px;padding:0 18px;border-radius:10px;border:1px solid #0b6b66;background:white;color:#0b6b66;font-weight:700;cursor:pointer;">{label}</button>
        """,
        height=height,
    )
