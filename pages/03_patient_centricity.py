import pandas as pd
import streamlit as st

from components.domain_workflow import render_domain_workflow
from components.guided_inputs import guided_text_area
from components.layout import page_header, safe_callout

page_header(
    "Patient-Centricity Studio",
    "Create empathetic, understandable and review-ready patient communication.",
    "Moderate",
)
render_domain_workflow(
    "patient",
    [
        "Explain a diagnosis in plain language",
        "Create medication counselling points",
        "Create discharge instructions",
        "Compare treatment options for shared decision-making",
        "Build a patient journey map",
        "Create teach-back questions",
        "Draft a caregiver follow-up message",
        "Develop a patient-experience improvement plan",
    ],
    [
        "Newly diagnosed type 2 diabetes",
        "Pre-procedure counselling",
        "Medication adherence barriers",
        "Post-discharge follow-up",
        "Caregiver support for chronic illness",
    ],
    "a clinician and patient-communication specialist",
    """- Do not individualise treatment changes or dosing.
- Avoid blame, stigma and unnecessary alarm.
- Include urgent red flags only when relevant.
- Require clinician review before patient use.""",
)

st.divider()
st.subheader("Interactive patient-journey mapping lab")
safe_callout(
    "Use an editable sample or build from scratch",
    "Select a fictional service scenario, load its sample journey, and edit every cell. Use only fictional or aggregate service information.",
)

SCENARIOS = {
    "Hypertension follow-up clinic": {
        "Access to care": {
            "Patient goal": "Get a convenient appointment",
            "Pain point": "Long booking wait and unclear slot availability",
            "Emotion": 2,
            "Severity": 4,
            "Information need": "Available channels, expected wait and preparation",
            "Stakeholder": "Scheduling team",
            "Improvement": "Offer clear digital and telephone booking pathways with reminders",
        },
        "Consultation": {
            "Patient goal": "Understand blood-pressure control and next steps",
            "Pain point": "Technical explanation and limited question time",
            "Emotion": 3,
            "Severity": 4,
            "Information need": "Plain-language meaning of readings and treatment goals",
            "Stakeholder": "Clinician",
            "Improvement": "Use a one-page explanation and teach-back questions",
        },
        "Treatment initiation": {
            "Patient goal": "Use medicines correctly",
            "Pain point": "Unclear timing, side effects and missed-dose guidance",
            "Emotion": 2,
            "Severity": 5,
            "Information need": "Medication purpose, schedule and warning signs",
            "Stakeholder": "Clinician / pharmacist",
            "Improvement": "Provide reviewed medication counselling and a simple schedule",
        },
        "Follow-up": {
            "Patient goal": "Know when and how to return",
            "Pain point": "No clear follow-up channel",
            "Emotion": 2,
            "Severity": 4,
            "Information need": "Review date, monitoring plan and contact route",
            "Stakeholder": "Care coordination team",
            "Improvement": "Send a de-identified template reminder with escalation instructions",
        },
    },
    "New diabetes diagnosis": {
        "Diagnosis": {
            "Patient goal": "Understand what the diagnosis means",
            "Pain point": "Fear, information overload and self-blame",
            "Emotion": 1,
            "Severity": 5,
            "Information need": "Plain-language explanation and common misconceptions",
            "Stakeholder": "Clinician / diabetes educator",
            "Improvement": "Use empathetic explanation, visuals and teach-back",
        },
        "Treatment initiation": {
            "Patient goal": "Know what to do first",
            "Pain point": "Too many simultaneous lifestyle and medication instructions",
            "Emotion": 2,
            "Severity": 5,
            "Information need": "Prioritised first-week action plan",
            "Stakeholder": "Care team",
            "Improvement": "Provide three prioritised actions and a reviewed written plan",
        },
        "Adherence": {
            "Patient goal": "Fit care into daily life",
            "Pain point": "Work schedule, cost and food-related barriers",
            "Emotion": 2,
            "Severity": 4,
            "Information need": "Practical options and support services",
            "Stakeholder": "Clinician / counsellor",
            "Improvement": "Discuss barriers non-judgementally and co-create feasible steps",
        },
        "Monitoring": {
            "Patient goal": "Understand progress",
            "Pain point": "Unclear interpretation of readings and tests",
            "Emotion": 3,
            "Severity": 3,
            "Information need": "What to monitor and when to seek help",
            "Stakeholder": "Clinician",
            "Improvement": "Create a simple monitoring guide with reviewed thresholds",
        },
    },
    "Post-discharge recovery": {
        "Discharge": {
            "Patient goal": "Leave with confidence",
            "Pain point": "Rushed instructions and multiple documents",
            "Emotion": 2,
            "Severity": 5,
            "Information need": "Medicines, activity, diet, warning signs and contacts",
            "Stakeholder": "Discharge team",
            "Improvement": "Use one consolidated reviewed discharge summary",
        },
        "Follow-up": {
            "Patient goal": "Recover safely at home",
            "Pain point": "Uncertainty about expected symptoms",
            "Emotion": 2,
            "Severity": 4,
            "Information need": "Expected course, red flags and appointment details",
            "Stakeholder": "Care coordination team",
            "Improvement": "Provide a caregiver-friendly follow-up checklist",
        },
    },
    "Build manually": {},
}

scenario = st.selectbox("Journey scenario", list(SCENARIOS), key="journey_scenario")
journey_goal = guided_text_area(
    "Journey-mapping objective",
    key="journey_objective",
    samples=[
        "Identify the three highest-priority patient pain points and propose feasible service improvements with responsible owners.",
        "Compare emotional burden and barrier severity across stages, then create a 30-day patient-experience action plan.",
        "Find communication failures across the journey and design plain-language, teach-back and follow-up interventions.",
    ],
    placeholder="Type the service-improvement question you want this journey map to answer.",
    height=110,
)

default_stages = [
    "Awareness",
    "Symptom recognition",
    "Access to care",
    "Consultation",
    "Investigation",
    "Diagnosis",
    "Treatment initiation",
    "Adherence",
    "Monitoring",
    "Follow-up",
    "Discharge",
]
scenario_stages = list(SCENARIOS[scenario])
selected_stages = st.multiselect(
    "Journey stages",
    default_stages,
    default=scenario_stages or ["Access to care", "Consultation", "Diagnosis", "Treatment initiation", "Follow-up"],
    key="journey_stages",
)

if "journey_editor_version" not in st.session_state:
    st.session_state["journey_editor_version"] = 0

c1, c2 = st.columns(2)
if c1.button("Load selected sample", use_container_width=True, disabled=scenario == "Build manually"):
    st.session_state["journey_loaded_scenario"] = scenario
    st.session_state["journey_editor_version"] += 1
    st.rerun()
if c2.button("Reset to blank table", use_container_width=True):
    st.session_state["journey_loaded_scenario"] = "Build manually"
    st.session_state["journey_editor_version"] += 1
    st.rerun()

loaded = st.session_state.get("journey_loaded_scenario", "Build manually")
source = SCENARIOS.get(loaded, {})
rows = []
for stage in selected_stages:
    item = source.get(stage, {})
    rows.append(
        {
            "Stage": stage,
            "Patient goal": item.get("Patient goal", ""),
            "Pain point": item.get("Pain point", ""),
            "Emotion (1–5)": item.get("Emotion", 3),
            "Barrier severity (1–5)": item.get("Severity", 3),
            "Information need": item.get("Information need", ""),
            "Responsible stakeholder": item.get("Stakeholder", ""),
            "Improvement idea": item.get("Improvement", ""),
        }
    )

journey = pd.DataFrame(rows)
edited_journey = st.data_editor(
    journey,
    use_container_width=True,
    hide_index=True,
    num_rows="dynamic",
    key=f"patient_journey_editor_{st.session_state['journey_editor_version']}",
    column_config={
        "Emotion (1–5)": st.column_config.NumberColumn(min_value=1, max_value=5, step=1),
        "Barrier severity (1–5)": st.column_config.NumberColumn(min_value=1, max_value=5, step=1),
    },
)

if not edited_journey.empty:
    scored = edited_journey.copy()
    scored["Priority score"] = scored["Barrier severity (1–5)"] * (6 - scored["Emotion (1–5)"])
    st.markdown("#### Priority view")
    st.caption(journey_goal or "Higher scores indicate a combination of severe barriers and negative patient emotion.")
    st.dataframe(
        scored.sort_values("Priority score", ascending=False),
        use_container_width=True,
        hide_index=True,
    )
    st.download_button(
        "Download journey map CSV",
        scored.to_csv(index=False).encode("utf-8"),
        "fictional_patient_journey_map.csv",
        "text/csv",
        use_container_width=True,
    )
