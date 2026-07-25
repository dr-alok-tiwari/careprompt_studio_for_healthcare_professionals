from __future__ import annotations

import streamlit as st

from components.guided_inputs import (
    choice_with_custom,
    guided_text_area,
    nudge_selector,
    starter_for_domain,
)
from components.layout import safe_callout
from components.prompt_ui import prompt_result
from services.prompt_engine import PromptInputs, build_craft_med
from services.safety_checker import inspect_text


AUDIENCES = [
    "Patient",
    "Caregiver",
    "Clinician",
    "Research team",
    "Medical affairs team",
    "Executive leadership",
    "Students / workshop participants",
]

OUTPUT_FORMATS = [
    "Structured report",
    "Plain-language script",
    "Checklist",
    "Comparison table",
    "Presentation outline",
    "One-page brief",
    "Email or message",
    "Patient handout",
]

TONES = [
    "Empathetic and reassuring",
    "Professional and concise",
    "Academic and evidence-focused",
    "Executive and action-oriented",
    "Patient-friendly and non-technical",
]


def render_domain_workflow(
    domain: str,
    workflows: list[str],
    examples: list[str],
    default_role: str,
    safeguards: str,
    risk: str = "Moderate",
) -> None:
    tab1, tab2, tab3 = st.tabs(["✨ Build a guided prompt", "💡 Try an example", "🛡️ Review safeguards"])

    with tab1:
        safe_callout(
            "How this works",
            "Choose a workflow, start from an editable example or type manually, add prompt nudges, then generate a ChatGPT-ready prompt.",
        )

        workflow = choice_with_custom(
            "Workflow",
            workflows,
            key=f"{domain}_workflow",
            custom_placeholder="Describe the exact healthcare task you need help with",
        )

        context = guided_text_area(
            "Fictional or de-identified context",
            key=f"{domain}_context",
            samples=starter_for_domain(domain, examples),
            placeholder="Describe the situation, objective and available information without identifiers.",
            help_text="Use age bands and broad chronology rather than identifiable details. The field remains fully editable.",
            height=190,
        )

        st.markdown("#### Shape the output")
        c1, c2, c3 = st.columns(3)
        with c1:
            audience = choice_with_custom(
                "Intended audience",
                AUDIENCES,
                key=f"{domain}_audience",
                custom_placeholder="Example: caregivers with limited health literacy",
            )
        with c2:
            output_format = choice_with_custom(
                "Output format",
                OUTPUT_FORMATS,
                key=f"{domain}_format",
                custom_placeholder="Example: two-column decision aid",
            )
        with c3:
            tone = choice_with_custom(
                "Tone",
                TONES,
                key=f"{domain}_tone",
                custom_placeholder="Example: calm, direct and culturally sensitive",
            )

        detail = st.select_slider(
            "Detail level",
            ["Concise", "Balanced", "Detailed"],
            value="Balanced",
            key=f"{domain}_detail",
            help="Balanced is recommended for most workshop and professional tasks.",
        )

        default_nudges = {
            "patient": ["Use plain, non-stigmatising language", "Use teach-back questions"],
            "clinical": ["Do not provide a final diagnosis", "Show supporting and opposing evidence"],
            "research": ["Flag every citation for source verification", "Check bias, confounding, leakage and selective reporting"],
            "pharma": ["Separate scientific evidence from promotional claims", "Mark items requiring medical-legal-regulatory review"],
            "pv": ["Verify chronology, dose, route, seriousness and outcome", "Require qualified pharmacovigilance review"],
            "projection": ["Do not exaggerate credentials or outcomes", "Use specific, verifiable achievements"],
        }
        nudges = nudge_selector(domain, key=f"{domain}_builder", defaults=default_nudges.get(domain, []))

        reviewer = st.text_input(
            "Required human reviewer",
            key=f"{domain}_reviewer",
            placeholder="Example: treating clinician, research supervisor, medical reviewer or PV physician",
            help="Name the role, not an identifiable person.",
        )

        generate = st.button(
            "Generate responsible ChatGPT prompt",
            type="primary",
            key=f"gen_{domain}",
            use_container_width=True,
        )
        if generate:
            combined = f"{workflow}\n{context}\n{reviewer}"
            safety = inspect_text(combined)
            if safety.flags:
                st.warning(
                    "Possible sensitive information detected: "
                    + ", ".join(safety.flags)
                    + ". The generated prompt uses the redacted version. Review it manually before copying."
                )

            safe_context = safety.sanitised_text.strip() or f"A fictional demonstration concerning: {workflow}."
            nudge_text = "\n- " + "\n- ".join(nudges) if nudges else ""
            reviewer_text = reviewer.strip() or "an appropriately qualified healthcare professional"

            prompt = build_craft_med(
                PromptInputs(
                    context=safe_context,
                    role=default_role,
                    audience=audience or "an appropriate professional audience",
                    format=f"{output_format or 'Structured response'}; {detail.lower()} detail; {tone or 'professional tone'}.",
                    task=workflow or "Complete the selected healthcare task.",
                    safeguards=(
                        safeguards
                        + nudge_text
                        + f"\n- State explicitly that final use requires review by {reviewer_text}."
                    ),
                    evidence=(
                        "Use verifiable and current sources when factual claims are made. "
                        "Do not invent citations. Mark claims, local policies and regulatory points requiring verification."
                    ),
                    details=(
                        "Use clear headings, empathetic and non-stigmatising language, and an action-oriented conclusion. "
                        "Begin with missing information or assumptions when these materially affect the answer."
                    ),
                )
            )
            st.session_state[f"last_{domain}_prompt"] = prompt
            prompt_result(prompt, save_key=domain)

    with tab2:
        st.markdown("#### One-click practice starters")
        st.caption("Loading an example fills the editable context field. You can then rewrite it completely.")
        starters = starter_for_domain(domain, examples)
        for index, example in enumerate(starters[:8]):
            with st.expander(f"Example {index + 1}: {example.split(':', 1)[0]}"):
                st.write(example)
                if st.button("Use this editable example", key=f"{domain}_load_example_{index}"):
                    st.session_state[f"{domain}_context_text"] = example
                    st.session_state.pop(f"{domain}_context_applied_sample", None)
                    st.success("Example loaded. Return to the first tab and edit it.")

    with tab3:
        st.markdown(f"**Workflow risk level:** {risk}")
        st.markdown(safeguards)
        st.markdown("#### Before using any generated output")
        checks = [
            "The input is fictional or appropriately de-identified.",
            "Critical facts, numbers, citations and guidelines have been independently verified.",
            "The output does not overstate certainty or professional authority.",
            "A qualified human reviewer has checked the final version.",
            "Local institutional, legal, regulatory and privacy requirements have been followed.",
        ]
        for index, item in enumerate(checks):
            st.checkbox(item, key=f"{domain}_safeguard_check_{index}")
