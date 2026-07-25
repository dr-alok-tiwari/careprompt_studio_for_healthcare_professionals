from components.layout import page_header
from components.domain_workflow import render_domain_workflow

page_header(
    "Research Studio",
    "Move from research idea to evidence synthesis, design, analysis and responsible academic writing.",
    "Moderate",
)
render_domain_workflow(
    "research",
    [
        "Convert an interest into a research problem",
        "Build PICO / PECO / SPIDER questions",
        "Generate a database search strategy",
        "Create inclusion and exclusion criteria",
        "Plan a systematic review",
        "Develop a statistical analysis plan",
        "Design a machine-learning validation strategy",
        "Critique a manuscript",
        "Draft a reviewer response",
        "Prepare a grant proposal outline",
    ],
    [
        "Medication adherence",
        "Antimicrobial resistance",
        "Medical imaging",
        "Maternal health",
        "Real-world evidence",
        "Patient satisfaction",
    ],
    "a clinical research methodologist and biostatistics-aware academic editor",
    """- Never fabricate data, results or references.
- Separate evidence supplied by the user from interpretation.
- Verify every citation in the original source.
- Flag risks of bias, leakage, confounding and selective reporting.
- Follow applicable journal and institutional AI-disclosure rules.""",
)
