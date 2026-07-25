import pandas as pd
import streamlit as st

from components.guided_inputs import (
    choice_with_custom,
    guided_text_area,
    nudge_selector,
    starter_for_domain,
)
from components.layout import page_header, safe_callout
from components.prompt_ui import prompt_result
from services.prompt_engine import PromptInputs, build_craft_med, evaluate_prompt, improve_prompt
from services.safety_checker import inspect_text
from utils.constants import AUDIENCES, FORMATS, ROLES
from utils.helpers import load_json

page_header(
    "Universal CRAFT-MED Prompt Builder",
    "Turn a healthcare task into a clear, evidence-aware and safety-conscious ChatGPT prompt—with editable examples at every major step.",
)

DOMAIN_LABELS = {
    "Patient communication": "patient",
    "Clinical reasoning education": "clinical",
    "Research and academic writing": "research",
    "Pharma and medical affairs": "pharma",
    "Pharmacovigilance": "pv",
    "Professional projection": "projection",
}

TASK_SAMPLES = {
    "patient": [
        "Explain the condition in plain language, correct common misconceptions, add teach-back questions, and create a clinician-review checklist.",
        "Create a one-page caregiver follow-up message with practical next steps and relevant warning signs.",
    ],
    "clinical": [
        "Structure a prioritised differential for educational review, identify missing information and red flags, and explicitly avoid a final diagnosis.",
        "Turn the fictional case into a concise referral question with relevant positives, negatives and uncertainty.",
    ],
    "research": [
        "Develop a research question, objectives, variables, feasible design, analysis plan, bias controls and reporting checklist.",
        "Create a reproducible database search strategy, eligibility criteria, extraction table and evidence-synthesis plan.",
    ],
    "pharma": [
        "Create a non-promotional scientific briefing that separates source evidence, interpretation, limitations and MLR review points.",
        "Develop an advisory-board discussion guide focused on unmet needs and evidence gaps without leading language.",
    ],
    "pv": [
        "Structure the fictional case narrative, identify missing follow-up information, and create a qualified-review checklist.",
        "Review chronology, seriousness, outcome and duplicate indicators without making unsupported causal claims.",
    ],
    "projection": [
        "Write a concise and a detailed professional biography using only verifiable achievements and a clear collaboration invitation.",
        "Improve the profile for clarity, authenticity and global professional positioning without exaggeration.",
    ],
}


tab1, tab2, tab3 = st.tabs(["✨ Guided builder", "📚 Prompt library", "📊 Prompt quality check"])

with tab1:
    safe_callout(
        "CRAFT-MED structure",
        "Context, Role, Audience, Format, Task, Medical safeguards, Evidence requirements and Details. Select a sample or type manually in every editable field.",
    )

    domain_label = st.selectbox("Task area", list(DOMAIN_LABELS), key="builder_domain")
    domain = DOMAIN_LABELS[domain_label]

    c1, c2 = st.columns(2)
    with c1:
        role = choice_with_custom(
            "Role for ChatGPT",
            ROLES,
            key="builder_role",
            custom_placeholder="Example: senior medical educator and patient-communication specialist",
        )
        context = guided_text_area(
            "C — Context",
            key=f"builder_context_{domain}",
            samples=starter_for_domain(domain),
            placeholder="Use fictional or de-identified information and explain what is already known.",
            height=170,
        )
        task = guided_text_area(
            "T — Exact task",
            key=f"builder_task_{domain}",
            samples=TASK_SAMPLES[domain],
            placeholder="State exactly what ChatGPT should produce, analyse or improve.",
            height=145,
        )
        audience = choice_with_custom(
            "A — Audience",
            AUDIENCES,
            key="builder_audience",
            custom_placeholder="Example: caregivers with limited health literacy",
        )

    with c2:
        output_format = choice_with_custom(
            "F — Format",
            FORMATS,
            key="builder_format",
            custom_placeholder="Example: one-page handout plus a 60-second counselling script",
        )
        evidence = guided_text_area(
            "E — Evidence requirements",
            key="builder_evidence",
            samples=[
                "Use verifiable current sources. Do not fabricate citations. For every important claim, state what should be checked in the original source.",
                "Use only evidence supplied by me. Separate direct evidence from interpretation and clearly label evidence gaps.",
                "Prioritise systematic reviews, professional guidelines and primary studies. Include DOI or official source details only when verified.",
            ],
            default="Use verifiable sources; do not fabricate references; flag claims requiring verification.",
            height=135,
        )
        details = guided_text_area(
            "D — Details and constraints",
            key="builder_details",
            samples=[
                "Use balanced detail, clear headings, empathetic professional language, a comparison table where useful, and a concise action-oriented conclusion.",
                "Create a one-page executive version followed by a detailed technical appendix. Clearly state assumptions and limitations.",
                "Adapt the content for Indian healthcare settings while flagging local policies and regulations that require verification.",
            ],
            default="Balanced detail; empathetic professional tone; clearly state assumptions and limitations.",
            height=135,
        )
        safeguards = guided_text_area(
            "M — Medical and professional safeguards",
            key=f"builder_safeguards_{domain}",
            samples=[
                "Do not provide autonomous diagnosis, prescribing, dosing, emergency or regulatory advice. Require qualified human review before use.",
                "Do not use identifiable patient, reporter or confidential organisational information. State uncertainty and stop when critical information is missing.",
                "Do not fabricate data, references, outcomes, credentials or claims. Separate facts, assumptions and recommendations.",
            ],
            default="Do not provide autonomous diagnosis, prescribing or dosing advice. Require qualified human review.",
            height=145,
        )

    nudges = nudge_selector(
        domain,
        key=f"universal_builder_{domain}",
        defaults=["List missing information before answering", "State uncertainty clearly", "Add a qualified human-review checklist"],
    )

    if st.button("Build expert prompt", type="primary", use_container_width=True):
        context_result = inspect_text(context)
        task_result = inspect_text(task)
        flags = list(dict.fromkeys(context_result.flags + task_result.flags))
        if flags:
            st.warning("Possible identifiers detected and redacted: " + ", ".join(flags))

        safe_context = context_result.sanitised_text.strip() or "No sensitive context supplied. Use a fictional demonstration."
        safe_task = task_result.sanitised_text.strip() or "Complete the selected healthcare task."
        nudge_text = "\n- " + "\n- ".join(nudges) if nudges else ""

        prompt = build_craft_med(
            PromptInputs(
                safe_context,
                role or "an appropriately qualified healthcare specialist",
                audience or "the intended professional audience",
                output_format or "a structured response",
                safe_task,
                safeguards + nudge_text,
                evidence,
                details,
            )
        )
        st.session_state["builder_prompt"] = prompt
        prompt_result(prompt, save_key="builder")

        scores = evaluate_prompt(prompt)
        average = sum(scores.values()) / max(len(scores), 1)
        st.markdown("#### Prompt scorecard")
        m1, m2 = st.columns([1, 3])
        m1.metric("Overall quality", f"{average:.1f}/10")
        m2.progress(min(int(average * 10), 100), text="CRAFT-MED completeness")
        st.dataframe(
            pd.DataFrame({"Dimension": scores.keys(), "Score / 10": scores.values()}),
            hide_index=True,
            use_container_width=True,
        )

with tab2:
    templates = load_json("prompt_templates.json")
    categories = ["All"] + sorted({item["category"] for item in templates})
    c1, c2 = st.columns([1, 2])
    with c1:
        category = st.selectbox("Category", categories, key="library_category")
    with c2:
        quick_search = st.selectbox(
            "Quick search nudge",
            ["Type manually", "patient education", "systematic review", "clinical reasoning", "medical affairs", "pharmacovigilance", "professional biography"],
            key="library_quick_search",
        )
        search_default = "" if quick_search == "Type manually" else quick_search
        search = st.text_input("Search templates", value=search_default, key="library_search")

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
    for item in subset[:40]:
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
    raw = guided_text_area(
        "Prompt to evaluate",
        key="quality_prompt",
        samples=[
            "Explain diabetes to a patient.",
            "Review this fictional clinical case and tell me the diagnosis.",
            "Write a literature review with 20 references and make it publishable.",
            "Create a professional biography that makes me look like a global expert.",
        ],
        placeholder="Paste or type a prompt. You can start with a weak sample and improve it.",
        height=220,
    )
    if st.button("Evaluate and improve prompt", type="primary", use_container_width=True) and raw.strip():
        scores = evaluate_prompt(raw)
        average = sum(scores.values()) / max(len(scores), 1)
        st.metric("Overall quality", f"{average:.1f}/10")
        st.bar_chart(pd.DataFrame({"Score": scores}).T)
        st.markdown("#### Suggested improved version")
        st.code(improve_prompt(raw), language="markdown", wrap_lines=True)
