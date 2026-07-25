import streamlit as st

def comparison_table(frame) -> None:
    st.dataframe(frame, use_container_width=True, hide_index=True)
