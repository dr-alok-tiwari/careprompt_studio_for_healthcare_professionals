import streamlit as st
from components.layout import page_header
from utils.helpers import load_json
from components.prompt_ui import prompt_result

page_header(
    "Interactive Case Simulator",
    "Practise prompt building, tool selection and critical review using fictional scenarios.",
)
cases = load_json("clinical_cases.json")
levels = sorted({case["level"] for case in cases})
professions = sorted({case["profession"] for case in cases})
c1, c2 = st.columns(2)
with c1:
    level = st.selectbox("Level", levels)
with c2:
    profession = st.selectbox("Profession", professions)
subset = [case for case in cases if case["level"] == level and case["profession"] == profession]
case = st.selectbox("Case", subset, format_func=lambda item: item["title"])
if case:
    st.markdown(f"### {case['title']}")
    st.write(case["scenario"])
    with st.expander("Available information", expanded=True):
        st.markdown("\n".join("- " + item for item in case["available_information"]))
    st.text_area(
        "What information is missing, and what should the AI be asked to do safely?",
        height=130,
    )
    if st.button("Reveal next stage"):
        st.markdown("#### Missing information")
        st.markdown("\n".join("- " + item for item in case["missing_information"]))
        st.markdown("#### Ethical and safety concern")
        st.warning(case["safety_concern"])
        prompt_result(case["model_prompt"], title="Model prompt", save_key=case["id"])
        st.markdown("#### Reflection")
        for question in case["reflection_questions"]:
            st.write("- " + question)
