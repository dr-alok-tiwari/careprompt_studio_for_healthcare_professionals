import streamlit as st
from components.copy_button import copy_button
from services.export_service import as_markdown


def prompt_result(prompt: str, title: str = "Your ChatGPT-ready prompt", save_key: str = "generated") -> None:
    st.markdown(f"### {title}")
    st.code(prompt, language="markdown", wrap_lines=True)
    c1, c2, c3 = st.columns([1,1,1])
    with c1:
        copy_button(prompt)
    with c2:
        st.download_button("Download .md", as_markdown(title, prompt), file_name="careprompt.md", mime="text/markdown")
    with c3:
        if st.button("Save to workspace", key=f"save_{save_key}"):
            st.session_state.setdefault("saved_prompts", []).append({"title": title, "prompt": prompt})
            st.success("Saved to My Workspace.")
