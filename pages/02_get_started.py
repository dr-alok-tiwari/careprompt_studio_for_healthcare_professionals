import streamlit as st

from components.guided_inputs import choice_with_custom, guided_text_area
from components.layout import page_header, safe_callout, step_card
from utils.constants import ROLES

page_header(
    "Get Started",
    "Personalise the app in under two minutes without entering sensitive information.",
)

safe_callout(
    "Your preferences stay in this browser session",
    "Do not enter patient, reporter or confidential organisational information. Use this page only to describe your professional goals.",
)

c1, c2 = st.columns(2)
with c1:
    role = choice_with_custom(
        "Your professional role",
        ROLES,
        key="onboarding_role",
        custom_placeholder="Example: hospital quality manager",
    )
    objective = choice_with_custom(
        "Primary objective",
        [
            "Patient communication",
            "Clinical reasoning education",
            "Research",
            "Pharma / medical affairs",
            "Pharmacovigilance",
            "Professional projection",
            "AI learning",
        ],
        key="onboarding_objective",
        custom_placeholder="Describe your main objective",
    )
    familiarity = st.radio(
        "AI familiarity",
        ["New to AI", "Comfortable", "Advanced"],
        horizontal=True,
        key="onboarding_familiarity",
    )
with c2:
    output = choice_with_custom(
        "Typical output needed",
        [
            "Prompt only",
            "Patient-facing content",
            "Research plan",
            "Briefing note",
            "Presentation",
            "Checklist",
        ],
        key="onboarding_output",
        custom_placeholder="Example: one-page workshop handout",
    )
    time_available = st.select_slider(
        "Time available",
        ["5 minutes", "15 minutes", "30 minutes", "60+ minutes"],
        value="15 minutes",
        key="onboarding_time",
    )
    explanation_level = st.radio(
        "Guidance style",
        ["Step-by-step", "Balanced", "Expert shortcuts"],
        horizontal=True,
        key="onboarding_guidance",
    )

first_task = guided_text_area(
    "First task you want to complete",
    key="onboarding_first_task",
    samples=[
        "Create a patient-friendly explanation of a chronic condition using plain language and teach-back questions.",
        "Develop a research question, search strategy and analysis outline for a healthcare study.",
        "Prepare a non-promotional medical-affairs briefing with evidence limitations and MLR review points.",
        "Improve my professional biography and collaboration pitch without exaggerating credentials.",
    ],
    placeholder="Type a non-sensitive professional task in your own words.",
    height=125,
)

if st.button("Save my preferences", type="primary", use_container_width=True):
    st.session_state.update(
        {
            "user_role": role or "Healthcare professional",
            "objective": objective or "AI learning",
            "familiarity": familiarity,
            "output_need": output or "Prompt only",
            "time_available": time_available,
            "guidance_style": explanation_level,
            "first_task": first_task,
            "onboarding_complete": True,
        }
    )
    st.success("Preferences saved for this session.")

if st.session_state.get("onboarding_complete"):
    st.subheader("Your recommended route")
    route_map = {
        "Patient communication": ("Patient-Centricity", "Prompt Builder", "Workspace"),
        "Clinical reasoning education": ("Clinical Reasoning", "Responsible AI", "Case Simulator"),
        "Research": ("Research Studio", "AI Tool Directory", "Workspace"),
        "Pharma / medical affairs": ("Pharma & Medical Affairs", "AI Tool Directory", "Facilitator Mode"),
        "Pharmacovigilance": ("Pharmacovigilance", "Responsible AI", "Case Simulator"),
        "Professional projection": ("Professional Projection", "Prompt Builder", "Workspace"),
        "AI learning": ("Learning Lab", "Case Simulator", "Prompt Builder"),
    }
    route = route_map.get(st.session_state.get("objective"), ("Prompt Builder", "AI Tool Directory", "Workspace"))
    for index, item in enumerate(route, start=1):
        step_card(index, item, "Complete this stage, then move to the next recommended module.")

    st.markdown("#### Continue")
    navigation_map = {
        "Patient communication": ("pages/03_patient_centricity.py", "Open Patient-Centricity Studio"),
        "Clinical reasoning education": ("pages/04_clinical_reasoning.py", "Open Clinical Reasoning"),
        "Research": ("pages/05_research_studio.py", "Open Research Studio"),
        "Pharma / medical affairs": ("pages/06_pharma_medical_affairs.py", "Open Medical Affairs Studio"),
        "Pharmacovigilance": ("pages/07_pharmacovigilance.py", "Open Pharmacovigilance Studio"),
        "Professional projection": ("pages/08_professional_projection.py", "Open Professional Projection"),
        "AI learning": ("pages/12_learning_lab.py", "Open Learning Lab"),
    }
    page, label = navigation_map.get(st.session_state.get("objective"), ("pages/09_prompt_builder.py", "Open Prompt Builder"))
    st.page_link(page, label=label, use_container_width=True)
