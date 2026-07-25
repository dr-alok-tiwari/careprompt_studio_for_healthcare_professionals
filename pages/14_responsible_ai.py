import streamlit as st

from components.guided_inputs import guided_text_area, starter_for_domain
from components.layout import page_header, safe_callout
from services.safety_checker import inspect_text

page_header(
    "Responsible AI & Privacy",
    "Use AI to support—not replace—professional judgement, validated systems and accountability.",
)

st.subheader("Four-step SAFE check")
cols = st.columns(4)
items = [
    ("S — Sensitivity", "Could this reveal a patient, reporter, organisation or confidential strategy?"),
    ("A — Authority", "Is the tool approved for this workflow and data class?"),
    ("F — Factuality", "Can every critical claim, number and citation be verified?"),
    ("E — Escalation", "Who must review the output before use or submission?"),
]
for col, (title, body) in zip(cols, items):
    col.markdown(
        f'<div class="cp-card"><h3>{title}</h3><p>{body}</p></div>',
        unsafe_allow_html=True,
    )

safe_callout(
    "Local pre-check only",
    "The checker looks for selected identifier patterns in your browser session. It cannot guarantee anonymisation, policy compliance or absence of re-identification risk.",
)

text = guided_text_area(
    "Text for a basic local pattern check",
    key="privacy_precheck",
    samples=starter_for_domain("privacy"),
    placeholder="Paste fictional or de-identified text, or select an example above.",
    help_text="Do not use this checker as permission to upload sensitive information to an external AI service.",
    height=180,
)

c1, c2 = st.columns([2, 1])
with c1:
    purpose = st.text_input(
        "Intended use",
        key="privacy_intended_use",
        placeholder="Example: internal educational workshop",
    )
with c2:
    reviewer = st.text_input(
        "Reviewer role",
        key="privacy_reviewer",
        placeholder="Example: treating clinician",
    )

if st.button("Run local SAFE pre-check", type="primary", use_container_width=True):
    result = inspect_text(text)
    m1, m2, m3 = st.columns(3)
    m1.metric("Preliminary risk", result.risk)
    m2.metric("Patterns flagged", str(len(result.flags)))
    m3.metric("Reviewer named", "Yes" if reviewer.strip() else "No")

    if result.flags:
        st.warning("Flags: " + ", ".join(result.flags))
        st.markdown("#### Redacted draft")
        st.code(result.sanitised_text, wrap_lines=True)
    else:
        st.success("No common identifier pattern was detected. Manual review is still required.")

    st.markdown("#### SAFE decision checklist")
    checklist = [
        "The information is fictional or appropriately de-identified.",
        "The selected AI tool is approved for this purpose and data class.",
        "The intended use has a legitimate professional or educational purpose.",
        "Critical facts and citations will be checked against original sources.",
        "A qualified reviewer has responsibility for the final output.",
    ]
    for index, item in enumerate(checklist):
        st.checkbox(item, key=f"safe_check_{index}")

st.subheader("Never use unsupervised AI for")
st.markdown(
    """- Final diagnosis, triage or treatment decisions
- Prescribing, dosing, changing or stopping medicines
- Emergency instructions
- Regulatory or pharmacovigilance submissions without qualified review
- Fabricating or filling missing research data
- Publishing unverified citations, numbers or claims
- Uploading identifiable patient, reporter or confidential organisational information to unapproved tools"""
)
