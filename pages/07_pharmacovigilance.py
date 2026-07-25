from components.layout import page_header
from components.domain_workflow import render_domain_workflow

page_header(
    "Pharmacovigilance Studio",
    "Structure fictional drug-safety workflows without replacing validated safety systems.",
    "Not suitable for unsupervised AI use",
)
render_domain_workflow(
    "pv",
    [
        "Structure an adverse-event narrative",
        "Generate case follow-up questions",
        "Review case completeness",
        "Create a seriousness checklist",
        "Discuss expectedness review steps",
        "Identify possible duplicate-case indicators",
        "Prepare a signal hypothesis",
        "Outline a benefit-risk discussion",
        "Analyse a fictional medication error",
    ],
    [
        "Suspected serious adverse reaction",
        "Incomplete spontaneous report",
        "Medication error",
        "Literature case",
        "Potential duplicate report",
    ],
    "a pharmacovigilance physician and case-processing quality reviewer",
    """- Do not enter identifiable patient or reporter information.
- Do not replace validated safety databases or coding dictionaries.
- Verify dates, dose, route, chronology, seriousness and outcome.
- Do not submit AI output without qualified pharmacovigilance review.
- Follow organisational and applicable regulatory procedures.""",
    "Not suitable for unsupervised AI use",
)
