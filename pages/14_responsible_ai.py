import streamlit as st
from components.layout import page_header
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
    col.markdown(f'<div class="cp-card"><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.subheader("Privacy pre-check")
text = st.text_area(
    "Paste text for a basic local pattern check",
    height=160,
    help="This local regex check is not a guarantee of anonymisation.",
)
if st.button("Check locally"):
    result = inspect_text(text)
    st.metric("Preliminary risk", result.risk)
    if result.flags:
        st.warning("Flags: " + ", ".join(result.flags))
        st.code(result.sanitised_text, wrap_lines=True)
    else:
        st.success("No common identifier pattern detected. Manual review is still required.")

st.subheader("Never use unsupervised AI for")
st.markdown(
    """- Final diagnosis or triage decisions
- Prescribing, dosing or stopping medicines
- Emergency instructions
- Regulatory or pharmacovigilance submission without qualified review
- Fabricating or filling missing research data
- Publishing unverified citations or claims"""
)
