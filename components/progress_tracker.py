import streamlit as st

def progress_tracker(completed: int, total: int, label: str = "Progress") -> None:
    ratio = 0 if total <= 0 else min(1.0, completed / total)
    st.progress(ratio, text=f"{label}: {completed}/{total}")
