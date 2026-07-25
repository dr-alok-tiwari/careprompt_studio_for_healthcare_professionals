from components.layout import page_header
from components.domain_workflow import render_domain_workflow

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

import pandas as pd
import streamlit as st

st.divider()
st.subheader("Interactive patient-journey mapping lab")
st.caption("Edit the table directly. Use fictional or aggregate service information only.")
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
]
selected_stages = st.multiselect(
    "Journey stages",
    default_stages,
    default=["Access to care", "Consultation", "Diagnosis", "Treatment initiation", "Follow-up"],
)
journey = pd.DataFrame(
    {
        "Stage": selected_stages,
        "Patient goal": ["" for _ in selected_stages],
        "Pain point": ["" for _ in selected_stages],
        "Emotion (1–5)": [3 for _ in selected_stages],
        "Barrier severity (1–5)": [3 for _ in selected_stages],
        "Information need": ["" for _ in selected_stages],
        "Responsible stakeholder": ["" for _ in selected_stages],
        "Improvement idea": ["" for _ in selected_stages],
    }
)
edited_journey = st.data_editor(
    journey,
    use_container_width=True,
    hide_index=True,
    num_rows="dynamic",
    key="patient_journey_editor",
)
if not edited_journey.empty:
    scored = edited_journey.copy()
    scored["Priority score"] = scored["Barrier severity (1–5)"] * (6 - scored["Emotion (1–5)"])
    st.markdown("#### Priority view")
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
    )
