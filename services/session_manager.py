import streamlit as st

DEFAULTS = {
    "experience_mode": "Beginner",
    "saved_prompts": [],
    "favourite_tools": [],
    "onboarding_complete": False,
    "learning_score": 0,
}

def initialise_session() -> None:
    for key, value in DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = value.copy() if isinstance(value, list) else value
