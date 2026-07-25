"""Reusable guided-input controls for novice and experienced healthcare users.

Every control offers a quick-start example while keeping the final field fully
editable. This reduces blank-page anxiety without forcing users into a template.
"""

from __future__ import annotations

from collections.abc import Iterable

import streamlit as st


DOMAIN_STARTERS: dict[str, list[str]] = {
    "patient": [
        "Fictional scenario: A 48-year-old adult has recently been diagnosed with type 2 diabetes and feels overwhelmed. Create a simple explanation, practical questions for the next consultation, and teach-back checks. Do not recommend individual treatment changes.",
        "Fictional scenario: A caregiver needs a clear post-discharge follow-up message for an older adult after a short hospital stay. Include warning signs, medication-adherence reminders, and when to contact the care team.",
        "Service-improvement scenario: Map the patient journey for people attending a hypertension clinic, focusing on appointment access, waiting, consultation clarity, medication understanding, and follow-up.",
    ],
    "clinical": [
        "Educational fictional case: An adult presents with chest discomfort of recent onset. Structure the history, identify missing information and red flags, and provide a prioritised differential for clinician review without giving a final diagnosis.",
        "Educational fictional case: A patient reports a persistent headache. Organise supporting and opposing evidence, missing examination details, urgent warning signs, and questions for qualified clinical evaluation.",
        "Educational fictional case: A patient develops a rash after starting a new medicine. Structure the chronology, possible alternative explanations, severity indicators, and escalation questions. Do not advise stopping or changing medication.",
    ],
    "research": [
        "Research idea: Investigate factors associated with medication adherence among adults with type 2 diabetes in outpatient care. Develop research questions, variables, a feasible design, analysis plan, bias controls, and a publication-ready reporting checklist.",
        "Systematic-review idea: Compare digital interventions for improving patient engagement in chronic disease management. Create PICO, databases, Boolean search strings, eligibility criteria, extraction fields, and synthesis plan.",
        "Machine-learning idea: Develop a clinically responsible prediction model using de-identified healthcare data. Specify split strategy, leakage prevention, calibration, fairness, interpretability, external validation, and transparent reporting.",
    ],
    "pharma": [
        "Medical-affairs scenario: Prepare a non-promotional MSL scientific briefing on newly published evidence. Separate source facts, interpretation, limitations, unanswered questions, and items requiring medical-legal-regulatory review.",
        "Congress scenario: Summarise fictional congress findings for an internal medical team, highlighting population, comparators, endpoints, effect estimates, safety, limitations, and implications without unsupported claims.",
        "Advisory-board scenario: Build a discussion guide on unmet patient needs, evidence gaps, treatment-pathway barriers, and future research questions. Avoid leading or promotional wording.",
    ],
    "pv": [
        "Fictional safety case: Structure an adverse-event narrative from de-identified details. Check chronology, suspect and concomitant products, dose, route, seriousness, outcome, missing information, and follow-up questions. Do not submit the output.",
        "Fictional safety case: Review an incomplete spontaneous report and identify the minimum case elements, missing clinical details, seriousness questions, duplicate indicators, and required qualified review.",
        "Fictional medication-error case: Organise what happened, contributing system factors, patient impact, immediate actions already taken, missing facts, and prevention questions without assigning blame.",
    ],
    "projection": [
        "Create an authentic 150-word professional biography for a healthcare academic. Emphasise current role, expertise, teaching, research, collaboration interests, and public value without exaggerating achievements.",
        "Improve a LinkedIn About section for a clinician-researcher who wants collaborations in AI-enabled healthcare. Use a confident but evidence-based tone and end with a specific collaboration invitation.",
        "Draft a concise conference-speaker introduction that highlights verified expertise, relevant work, and session value without unsupported superlatives.",
    ],
    "tool": [
        "Find and organise traceable evidence for a healthcare literature review using free or freemium tools.",
        "Create patient-friendly educational material without entering identifiable patient information.",
        "Analyse a de-identified CSV and create transparent charts, summary statistics, and an interpretation checklist.",
        "Prepare a scientific presentation with citations, speaker notes, and editable visuals.",
    ],
    "privacy": [
        "Fictional patient, aged 50–60, attended an outpatient clinic for follow-up. No name, phone number, address, record number, exact birth date, image, or unique identifier is included.",
        "A de-identified adverse-event summary containing only age band, broad chronology, suspect medicine, event, seriousness status, and outcome.",
    ],
}


GLOBAL_NUDGES = [
    "List missing information before answering",
    "State uncertainty clearly",
    "Do not fabricate references, guidelines, numbers or quotations",
    "Separate verified facts, assumptions, interpretation and recommendations",
    "Use only fictional or de-identified information",
    "Add a qualified human-review checklist",
    "Identify possible bias, exclusions and alternative explanations",
    "Provide a concise action-oriented summary",
]

DOMAIN_NUDGES: dict[str, list[str]] = {
    "patient": [
        "Use plain, non-stigmatising language",
        "Use teach-back questions",
        "Adapt to the stated health-literacy level",
        "Include relevant red flags without unnecessary alarm",
        "Create a caregiver-friendly version",
    ],
    "clinical": [
        "Do not provide a final diagnosis",
        "Show supporting and opposing evidence",
        "Prioritise emergency red flags",
        "Do not prescribe, change doses or advise stopping medicines",
        "Suggest questions for qualified clinical evaluation",
    ],
    "research": [
        "Distinguish supplied evidence from AI-generated interpretation",
        "Check bias, confounding, leakage and selective reporting",
        "Include reproducibility and reporting-standard checks",
        "Propose a feasible validation strategy",
        "Flag every citation for source verification",
    ],
    "pharma": [
        "Separate scientific evidence from promotional claims",
        "Mark items requiring medical-legal-regulatory review",
        "Verify indication, population, comparator and endpoints",
        "Include evidence limitations and unanswered questions",
        "Avoid confidential or unapproved information",
    ],
    "pv": [
        "Verify chronology, dose, route, seriousness and outcome",
        "Identify missing follow-up information",
        "Do not replace validated safety databases or dictionaries",
        "Require qualified pharmacovigilance review",
        "Avoid causal certainty unless supported",
    ],
    "projection": [
        "Do not exaggerate credentials or outcomes",
        "Use specific, verifiable achievements",
        "Protect confidential and patient information",
        "End with a clear collaboration or engagement invitation",
        "Offer concise and detailed versions",
    ],
}


def guided_text_area(
    label: str,
    *,
    key: str,
    samples: Iterable[str] | None = None,
    placeholder: str = "Type your own details here…",
    help_text: str | None = None,
    height: int = 150,
    default: str = "",
) -> str:
    """Render a sample selector followed by a completely editable text area."""

    sample_items = [item for item in (samples or []) if item]
    text_key = f"{key}_text"
    sample_key = f"{key}_sample"
    applied_key = f"{key}_applied_sample"

    if text_key not in st.session_state:
        st.session_state[text_key] = default

    if sample_items:
        selected = st.selectbox(
            f"Quick-start example for {label.lower()}",
            ["Choose a sample or write manually"] + sample_items,
            key=sample_key,
            help="Selecting a sample fills the editable field below. You can change every word.",
        )
        if selected != "Choose a sample or write manually" and st.session_state.get(applied_key) != selected:
            st.session_state[text_key] = selected
            st.session_state[applied_key] = selected

    value = st.text_area(
        label,
        key=text_key,
        height=height,
        placeholder=placeholder,
        help=help_text,
    )

    c1, c2 = st.columns([1, 4])
    if c1.button("Clear", key=f"{key}_clear", use_container_width=True):
        st.session_state[text_key] = ""
        st.session_state.pop(applied_key, None)
        st.rerun()
    c2.caption("The quick-start text is only a nudge. Edit it freely and remove anything not relevant.")
    return value


def choice_with_custom(
    label: str,
    options: Iterable[str],
    *,
    key: str,
    custom_placeholder: str,
    default_index: int = 0,
) -> str:
    """Render a selectbox with a manual custom option."""

    option_list = list(options)
    custom_label = "Other — type manually"
    selected = st.selectbox(label, option_list + [custom_label], index=default_index, key=f"{key}_choice")
    if selected == custom_label:
        return st.text_input(
            f"Custom {label.lower()}",
            key=f"{key}_custom",
            placeholder=custom_placeholder,
        ).strip()
    return selected


def nudge_selector(domain: str, *, key: str, defaults: Iterable[str] | None = None) -> list[str]:
    """Offer curated nudges plus a free-text instruction box."""

    options = list(dict.fromkeys(GLOBAL_NUDGES + DOMAIN_NUDGES.get(domain, [])))
    selected = st.multiselect(
        "Prompt nudges",
        options,
        default=[item for item in (defaults or []) if item in options],
        key=f"{key}_nudges",
        help="Select any number of instructions. Add your own instruction below.",
    )
    custom = st.text_area(
        "Your own nudge or constraint",
        key=f"{key}_custom_nudge",
        height=90,
        placeholder="Example: Use an Indian healthcare context and give a one-page version for senior clinicians.",
    )
    custom_items = [line.strip(" -•\t") for line in custom.splitlines() if line.strip()]
    return selected + custom_items


def starter_for_domain(domain: str, examples: Iterable[str] | None = None) -> list[str]:
    """Return rich domain starters and lightweight examples supplied by a page."""

    rich = DOMAIN_STARTERS.get(domain, [])
    lightweight = [f"Fictional practice scenario: {item}. Add only de-identified context and state the intended outcome." for item in (examples or [])]
    return list(dict.fromkeys(rich + lightweight))
