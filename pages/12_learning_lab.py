import streamlit as st

from components.layout import page_header, safe_callout
from utils.helpers import load_json

page_header(
    "Learning Lab",
    "Short lessons, myths and 500 case-based MCQs for responsible healthcare AI use.",
)
lessons = load_json("lessons.json")
quizzes = load_json("quizzes.json")
tab1, tab2, tab3 = st.tabs(["Micro-lessons", "Myth vs fact", "500-MCQ practice"])
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
    safe_callout(
        "Practice without accidental answer cues",
        "Choose an option, then use the individual reveal button to see the correct answer and explanation. Filter the 500-question bank by topic and difficulty.",
    )

    topics = sorted({question["topic"] for question in quizzes})
    difficulties = ["Foundation", "Intermediate", "Advanced"]
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1:
        topic_filter = st.selectbox(
            "Topic",
            ["All topics"] + topics,
            key="quiz_topic_filter",
        )
    with c2:
        difficulty_filter = st.selectbox(
            "Difficulty",
            ["All levels"] + difficulties,
            key="quiz_difficulty_filter",
        )
    with c3:
        page_size = st.selectbox(
            "Questions per page",
            [5, 10, 20],
            index=1,
            key="quiz_page_size",
        )

    filtered = [
        question
        for question in quizzes
        if (topic_filter == "All topics" or question["topic"] == topic_filter)
        and (
            difficulty_filter == "All levels"
            or question["difficulty"] == difficulty_filter
        )
    ]
    total_pages = max(1, (len(filtered) + page_size - 1) // page_size)
    page_key = (
        "quiz_page_"
        + topic_filter.replace(" ", "_")
        + "_"
        + difficulty_filter.replace(" ", "_")
        + f"_{page_size}"
    )
    page_number = int(
        st.number_input(
            "Page",
            min_value=1,
            max_value=total_pages,
            value=1,
            step=1,
            key=page_key,
        )
    )
    start = (page_number - 1) * page_size
    visible = filtered[start : start + page_size]
    st.caption(
        f"Showing {start + 1}–{start + len(visible)} of {len(filtered)} questions "
        f"· Page {page_number} of {total_pages}"
    )

    revealed_key = "learning_lab_revealed_questions"
    if revealed_key not in st.session_state:
        st.session_state[revealed_key] = []
    revealed = set(st.session_state[revealed_key])

    visible_results = []
    for question in visible:
        question_id = question["id"]
        with st.container(border=True):
            st.caption(
                f"{question_id} · {question['topic']} · {question['difficulty']} "
                f"· {question['context']}"
            )
            selected = st.radio(
                question["question"],
                question["options"],
                key=f"quiz_answer_{question_id}",
                index=None,
            )
            if st.button(
                "Reveal answer and explanation",
                key=f"quiz_reveal_{question_id}",
                use_container_width=True,
            ):
                revealed.add(question_id)
                st.session_state[revealed_key] = sorted(revealed)

            if question_id in revealed:
                st.markdown(f"**Correct answer:** {question['answer']}")
                if selected is None:
                    st.info(question["explanation"])
                elif selected == question["answer"]:
                    st.success("Correct. " + question["explanation"])
                else:
                    st.error("Not quite. " + question["explanation"])
            else:
                st.caption("Answer remains hidden until you select Reveal answer and explanation.")
            visible_results.append((question, selected))

    attempted = sum(
        selected is not None and question["id"] in revealed
        for question, selected in visible_results
    )
    correct = sum(
        selected == question["answer"] and question["id"] in revealed
        for question, selected in visible_results
    )
    accuracy = round((correct / attempted) * 100) if attempted else 0

    s1, s2, s3 = st.columns(3)
    with s1:
        revealed_on_page = sum(q["id"] in revealed for q in visible)
        st.metric("Revealed on this page", f"{revealed_on_page}/{len(visible)}")
    with s2:
        st.metric("Correct after reveal", f"{correct}/{attempted}")
    with s3:
        st.metric("Current accuracy", f"{accuracy}%")

    if attempted >= 10 and accuracy >= 80:
        st.success("Completion badge earned: Responsible Healthcare AI Foundations")
