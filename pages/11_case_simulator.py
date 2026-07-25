import streamlit as st

from components.guided_inputs import guided_text_area, nudge_selector
from components.layout import page_header, safe_callout
from components.prompt_ui import prompt_result
from utils.helpers import load_json

page_header(
    "Interactive Case Simulator",
    "Practise prompt building, tool selection and critical review using fictional healthcare scenarios.",
)

cases = load_json("clinical_cases.json")
levels = sorted({case["level"] for case in cases})
professions = sorted({case["profession"] for case in cases})

safe_callout(
    "Practice safely",
    "All cases are fictional. Write your own response, use a guided nudge if helpful, then compare it with the model prompt.",
)

c1, c2 = st.columns(2)
with c1:
    level = st.selectbox("Level", levels, key="case_level")
with c2:
    profession = st.selectbox("Profession", professions, key="case_profession")

subset = [case for case in cases if case["level"] == level and case["profession"] == profession]
if not subset:
    st.info("No case is available for this combination. Select another level or profession.")
    st.stop()

case = st.selectbox("Case", subset, format_func=lambda item: item["title"], key="case_selected")

st.markdown(f"### {case['title']}")
st.write(case["scenario"])
with st.expander("Available information", expanded=True):
    st.markdown("\n".join("- " + item for item in case["available_information"]))

response_samples = [
    "First identify the information required to understand the case safely. Then specify what AI may structure, what it must not decide, how uncertainty should be shown, and who must review the output.",
    "Ask the AI to separate available facts, missing facts, assumptions, risks, alternative explanations and next questions. Require verification and qualified human review.",
    "Create a CRAFT-MED prompt with a fictional context, exact task, intended audience, output format, evidence boundaries, privacy safeguards and escalation rules.",
]

learner_response = guided_text_area(
    "Your analysis and proposed AI instruction",
    key=f"case_response_{case['id']}",
    samples=response_samples,
    placeholder="Type what is missing, what the AI should do, what it must avoid, and who should review the result.",
    height=170,
)

nudges = nudge_selector(
    "clinical" if profession.lower().startswith("doctor") else "research",
    key=f"case_nudges_{case['id']}",
    defaults=["List missing information before answering", "State uncertainty clearly", "Add a qualified human-review checklist"],
)

if st.button("Reveal model stage and compare", type="primary", use_container_width=True):
    if learner_response.strip():
        st.markdown("#### Your response")
        st.write(learner_response)
        if nudges:
            st.caption("Selected nudges: " + " · ".join(nudges))
    else:
        st.info("You can still review the model stage, but writing your own response first gives better practice.")

    st.markdown("#### Missing information")
    st.markdown("\n".join("- " + item for item in case["missing_information"]))
    st.markdown("#### Ethical and safety concern")
    st.warning(case["safety_concern"])
    prompt_result(case["model_prompt"], title="Model prompt", save_key=case["id"])
    st.markdown("#### Reflection")
    for index, question in enumerate(case["reflection_questions"], start=1):
        st.write(f"{index}. {question}")

    st.markdown("#### Self-review")
    review_items = [
        "I identified missing information before asking for an answer.",
        "I stated what the AI must not decide autonomously.",
        "I included privacy, evidence and uncertainty safeguards.",
        "I named an appropriate qualified reviewer.",
    ]
    for index, item in enumerate(review_items):
        st.checkbox(item, key=f"case_review_{case['id']}_{index}")
