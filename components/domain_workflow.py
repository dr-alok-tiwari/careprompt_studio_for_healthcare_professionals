import streamlit as st
from components.prompt_ui import prompt_result
from services.prompt_engine import PromptInputs, build_craft_med
from services.safety_checker import inspect_text


def render_domain_workflow(
    domain: str,
    workflows: list[str],
    examples: list[str],
    default_role: str,
    safeguards: str,
    risk: str = "Moderate",
) -> None:
    tab1, tab2, tab3 = st.tabs(["Build a prompt", "Examples", "Review safeguards"])
    with tab1:
        workflow = st.selectbox("Choose a workflow", workflows)
        user_input = st.text_area(
            "Enter fictional or de-identified context",
            height=150,
            placeholder="Describe the situation without names or identifiers.",
        )
        audience = st.selectbox(
            "Intended audience",
            ["Patient", "Caregiver", "Clinician", "Research team", "Medical affairs team", "Executive leadership"],
        )
        output_format = st.selectbox(
            "Output format",
            ["Structured report", "Plain-language script", "Checklist", "Comparison table", "Presentation outline", "One-page brief"],
        )
        detail = st.select_slider("Detail level", ["Concise", "Balanced", "Detailed"], value="Balanced")
        nudges = st.multiselect(
            "Add prompt nudges",
            [
                "List missing information first",
                "State uncertainty",
                "Do not fabricate references",
                "Separate facts and assumptions",
                "Include red flags",
                "Add a human-review checklist",
                "Adapt for Indian healthcare settings",
                "Use teach-back questions",
            ],
        )
        if st.button("Generate safe prompt", type="primary", key=f"gen_{domain}"):
            safety = inspect_text(user_input)
            if safety.flags:
                st.warning(
                    "Possible sensitive information detected: "
                    + ", ".join(safety.flags)
                    + ". The prompt uses a redacted version."
                )
            context = safety.sanitised_text or f"A fictional demonstration concerning: {workflow}."
            nudge_text = "\n- " + "\n- ".join(nudges) if nudges else ""
            prompt = build_craft_med(
                PromptInputs(
                    context=context,
                    role=default_role,
                    audience=audience,
                    format=f"{output_format}; {detail.lower()} detail.",
                    task=workflow,
                    safeguards=safeguards + nudge_text,
                    evidence="Use verifiable, current sources when factual claims are made. Mark anything requiring local policy verification.",
                    details="Use empathetic, non-stigmatising language. Provide a concise action-oriented conclusion.",
                )
            )
            st.session_state[f"last_{domain}_prompt"] = prompt
            prompt_result(prompt, save_key=domain)
    with tab2:
        st.markdown("#### Fictional examples")
        for example in examples:
            with st.expander(example):
                st.write(
                    f"Use the guided builder to create a safe, audience-specific prompt for **{example}**. "
                    "Start by identifying missing facts and the appropriate human reviewer."
                )
    with tab3:
        st.markdown(f"**Workflow risk level:** {risk}")
        st.markdown(safeguards)
