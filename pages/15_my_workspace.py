import streamlit as st
import json
from components.layout import page_header
from services.export_service import as_docx, as_pdf

page_header("My Workspace", "Save, compare and export prompts during this browser session. Do not store sensitive information.")
saved=st.session_state.get("saved_prompts", [])
if not saved: st.info("No prompts saved yet. Use any studio or Prompt Builder and select ‘Save to workspace’.")
for i,item in enumerate(saved):
    with st.expander(f"{i+1}. {item['title']}"):
        st.code(item['prompt'], language="markdown", wrap_lines=True)
        c1,c2,c3=st.columns(3)
        c1.download_button("DOCX", as_docx(item['title'],item['prompt']), f"prompt_{i+1}.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"docx{i}")
        c2.download_button("PDF", as_pdf(item['title'],item['prompt']), f"prompt_{i+1}.pdf", "application/pdf", key=f"pdf{i}")
        if c3.button("Delete", key=f"delete{i}"):
            saved.pop(i); st.rerun()
if saved:
    st.download_button("Export workspace JSON", json.dumps(saved,indent=2).encode(), "careprompt_workspace.json", "application/json")
st.divider()
if st.button("Delete all session data"):
    for key in list(st.session_state.keys()): del st.session_state[key]
    st.success("Session data cleared."); st.rerun()
