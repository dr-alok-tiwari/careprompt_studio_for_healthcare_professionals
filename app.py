import streamlit as st

from config.app_config import APP_NAME, APP_TAGLINE
from components.layout import apply_theme, render_footer, render_privacy_banner
from services.session_manager import initialise_session

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_theme()
initialise_session()

pages = {
    "Start": [
        st.Page("pages/01_home.py", title="Home", icon="🏠", default=True),
        st.Page("pages/02_get_started.py", title="Get Started", icon="🧭"),
    ],
    "Work Studios": [
        st.Page("pages/03_patient_centricity.py", title="Patient-Centricity", icon="🤝"),
        st.Page("pages/04_clinical_reasoning.py", title="Clinical Reasoning", icon="🩺"),
        st.Page("pages/05_research_studio.py", title="Research Studio", icon="🔬"),
        st.Page("pages/06_pharma_medical_affairs.py", title="Pharma & Medical Affairs", icon="💊"),
        st.Page("pages/07_pharmacovigilance.py", title="Pharmacovigilance", icon="🛡️"),
        st.Page("pages/08_professional_projection.py", title="Professional Projection", icon="📣"),
    ],
    "AI Workbench": [
        st.Page("pages/09_prompt_builder.py", title="Prompt Builder", icon="✨"),
        st.Page("pages/10_ai_tool_directory.py", title="AI Tool Directory", icon="🧰"),
        st.Page("pages/11_case_simulator.py", title="Case Simulator", icon="🧩"),
        st.Page("pages/12_learning_lab.py", title="Learning Lab", icon="🎓"),
    ],
    "Resources": [
        st.Page("pages/13_resource_library.py", title="Resource Library", icon="📚"),
        st.Page("pages/14_responsible_ai.py", title="Responsible AI", icon="⚖️"),
        st.Page("pages/15_my_workspace.py", title="My Workspace", icon="🗂️"),
        st.Page("pages/16_facilitator_mode.py", title="Facilitator Mode", icon="🎤"),
        st.Page("pages/17_about.py", title="About", icon="ℹ️"),
    ],
}

with st.sidebar:
    st.markdown(f"## 🩺 {APP_NAME}")
    st.caption(APP_TAGLINE)
    st.divider()
    mode = st.radio(
        "Experience",
        options=["Beginner", "Advanced"],
        horizontal=True,
        key="experience_mode",
    )
    st.caption("No patient-identifiable data. Human review is required for high-risk outputs.")

render_privacy_banner()
nav = st.navigation(pages, position="sidebar", expanded=True)
nav.run()
render_footer()
