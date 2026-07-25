import streamlit as st

from components.copy_button import copy_button
from services.export_service import as_markdown


def prompt_result(prompt: str, title: str = "Your ChatGPT-ready prompt", save_key: str = "generated") -> None:
    st.markdown(f"### {title}")
    st.markdown(
        '<div class="cp-info"><b>Review before use:</b> remove irrelevant details, verify critical facts and citations, and keep a qualified professional responsible for the final output.</div>',
        unsafe_allow_html=True,
    )
    st.code(prompt, language="markdown", wrap_lines=True)

    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        copy_button(prompt, label="Copy prompt")
    with c2:
        st.download_button(
            "Download Markdown",
            as_markdown(title, prompt),
            file_name=f"careprompt_{save_key}.md",
            mime="text/markdown",
            key=f"download_{save_key}",
            use_container_width=True,
        )
    with c3:
        if st.button("Save to workspace", key=f"save_{save_key}", use_container_width=True):
            saved = st.session_state.setdefault("saved_prompts", [])
            duplicate = any(item.get("prompt") == prompt for item in saved)
            if duplicate:
                st.info("This prompt is already in My Workspace.")
            else:
                saved.append({"title": title, "prompt": prompt})
                st.success("Saved to My Workspace.")
