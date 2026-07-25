import streamlit as st


def feedback_widget(key: str = "feedback") -> None:
    rating = st.feedback("faces", key=f"{key}_rating")
    if rating is not None:
        st.caption("Thank you. Feedback is retained only in this session in the default build.")
