import streamlit as st
from components.layout import page_header
from utils.helpers import load_json

page_header(
    "Learning Lab",
    "Short lessons, myths and case-based quizzes for responsible healthcare AI use.",
)
lessons = load_json("lessons.json")
quizzes = load_json("quizzes.json")
tab1, tab2, tab3 = st.tabs(["Micro-lessons", "Myth vs fact", "Quiz"])
with tab1:
    for lesson in lessons:
        with st.expander(f"{lesson['title']} · {lesson['duration']}"):
            st.write(lesson["summary"])
            st.info(lesson["takeaway"])
with tab2:
    myths = [
        ("AI output is objective", "False. Models can reproduce bias, omit context and sound confident when wrong."),
        ("A citation-looking reference is reliable", "False. Verify the original source, DOI, authors, journal and claim."),
        ("De-identification removes every privacy risk", "False. Re-identification and organisational policy risks may remain."),
        ("A longer prompt always gives a better answer", "False. Relevance, structure and verification matter more than length."),
    ]
    for myth, fact in myths:
        st.markdown(f"**Myth:** {myth}\n\n**Fact:** {fact}")
with tab3:
    score = 0
    for i, question in enumerate(quizzes[:10]):
        answer = st.radio(question["question"], question["options"], key=f"q{i}", index=None)
        if answer:
            if answer == question["answer"]:
                st.success(question["explanation"])
                score += 1
            else:
                st.error(question["explanation"])
    st.metric("Current score", f"{score}/10")
    if score >= 8:
        st.success("Completion badge earned: Responsible Healthcare AI Foundations")
