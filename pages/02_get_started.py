import streamlit as st
from components.layout import page_header
from utils.constants import ROLES

page_header("Get Started", "Personalise the app in under one minute without entering sensitive information.")
with st.form("onboarding"):
    role = st.selectbox("Your professional role", ROLES)
    objective = st.selectbox("Primary objective", ["Patient communication", "Clinical reasoning education", "Research", "Pharma / medical affairs", "Pharmacovigilance", "Professional projection", "AI learning"])
    familiarity = st.radio("AI familiarity", ["New to AI", "Comfortable", "Advanced"], horizontal=True)
    output = st.selectbox("Typical output needed", ["Prompt only", "Patient-facing content", "Research plan", "Briefing note", "Presentation", "Checklist"])
    time = st.select_slider("Time available", ["5 minutes", "15 minutes", "30 minutes", "60+ minutes"], value="15 minutes")
    submitted = st.form_submit_button("Save preferences", type="primary")
if submitted:
    st.session_state.update({"user_role":role,"objective":objective,"familiarity":familiarity,"output_need":output,"time_available":time,"onboarding_complete":True})
    st.success("Preferences saved for this session.")

if st.session_state.get("onboarding_complete"):
    st.subheader("Recommended route")
    route_map = {
        "Patient communication":"Patient-Centricity → Prompt Builder → Workspace",
        "Clinical reasoning education":"Clinical Reasoning → Responsible AI → Case Simulator",
        "Research":"Research Studio → AI Tool Directory → Workspace",
        "Pharma / medical affairs":"Pharma & Medical Affairs → Tool Directory → Facilitator Mode",
        "Pharmacovigilance":"Pharmacovigilance → Responsible AI → Case Simulator",
        "Professional projection":"Professional Projection → Prompt Builder → Workspace",
        "AI learning":"Learning Lab → Case Simulator → Prompt Builder",
    }
    st.success(route_map.get(st.session_state.get("objective"), "Prompt Builder → Tool Directory"))
