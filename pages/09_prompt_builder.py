import streamlit as st
import pandas as pd
from components.layout import page_header
from components.prompt_ui import prompt_result
from services.prompt_engine import PromptInputs, build_craft_med, evaluate_prompt, improve_prompt
from services.safety_checker import inspect_text
from utils.constants import ROLES, AUDIENCES, FORMATS
from utils.helpers import load_json

page_header(
    "Universal CRAFT-MED Prompt Builder",
    "Turn a task into a clear, evidence-aware and safety-conscious ChatGPT prompt.",
)
tab1, tab2, tab3 = st.tabs(["Guided builder", "Prompt library", "Prompt quality check"])
with tab1:
    c1, c2 = st.columns(2)
    with c1:
        role = st.selectbox("C — Role for ChatGPT", ROLES)
        context = st.text_area("C — Context", placeholder="Use fictional or de-identified information.", height=120)
        task = st.text_area("T — Exact task", placeholder="What should ChatGPT produce or analyse?", height=100)
        audience = st.selectbox("A — Audience", AUDIENCES)
    with c2:
        fmt = st.selectbox("F — Format", FORMATS)
        evidence = st.text_area(
            "E — Evidence requirements",
            value="Use verifiable sources; do not fabricate references; flag claims requiring verification.",
        )
        details = st.text_area(
            "D — Details and constraints",
            value="Balanced detail; empathetic professional tone; clearly state assumptions and limitations.",
        )
        safeguards = st.text_area(
            "M — Medical safeguards",
            value="Do not provide autonomous diagnosis, prescribing or dosing advice. Require qualified human review.",
        )
    nudges = st.multiselect(
        "Predefined nudges",
        [
            "List missing information first",
            "State uncertainty",
            "Use only evidence I provide",
            "Separate facts, assumptions and recommendations",
            "Include red flags",
            "Add clinician-review checklist",
            "Adapt for Indian healthcare settings",
            "Generate three alternatives",
            "Critique your own response",
            "Identify possible bias",
            "Use fictional data only",
        ],
    )
    if st.button("Build expert prompt", type="primary"):
        result = inspect_text(context + "\n" + task)
        if result.flags:
            st.warning("Possible identifiers detected and redacted: " + ", ".join(result.flags))
        nudge_text = "\n- " + "\n- ".join(nudges) if nudges else ""
        prompt = build_craft_med(
            PromptInputs(
                result.sanitised_text or "No sensitive context supplied.",
                role,
                audience,
                fmt,
                task or "Complete the selected healthcare task.",
                safeguards + nudge_text,
                evidence,
                details,
            )
        )
        st.session_state["builder_prompt"] = prompt
        prompt_result(prompt, save_key="builder")
        scores = evaluate_prompt(prompt)
        st.markdown("#### Prompt scorecard")
        st.dataframe(
            pd.DataFrame({"Dimension": scores.keys(), "Score / 10": scores.values()}),
            hide_index=True,
            use_container_width=True,
        )
with tab2:
    templates = load_json("prompt_templates.json")
    categories = ["All"] + sorted({item["category"] for item in templates})
    category = st.selectbox("Category", categories)
    search = st.text_input("Search templates")
    subset = [
        item
        for item in templates
        if (category == "All" or item["category"] == category)
        and (
            not search
            or search.lower()
            in (item["title"] + item["prompt_template"] + " " + " ".join(item["tags"])).lower()
        )
    ]
    st.caption(f"{len(subset)} templates found")
    for item in subset[:30]:
        with st.expander(f"{item['title']} · {item['difficulty']} · {item['risk_level']}"):
            st.write(item["expected_output"])
            st.code(item["prompt_template"], language="markdown", wrap_lines=True)
            st.caption(
                "Free alternative: "
                + item["free_alternative"]
                + " | Specialised/paid: "
                + item["paid_alternative"]
            )
with tab3:
    raw = st.text_area("Paste a prompt to evaluate", height=220)
    if st.button("Evaluate prompt") and raw:
        scores = evaluate_prompt(raw)
        st.bar_chart(pd.DataFrame({"Score": scores}).T)
        st.code(improve_prompt(raw), language="markdown", wrap_lines=True)
