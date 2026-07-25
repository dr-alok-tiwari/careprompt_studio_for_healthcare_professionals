from components.layout import page_header
from components.domain_workflow import render_domain_workflow

page_header(
    "Professional Projection",
    "Build authentic professional visibility without exaggeration or confidentiality breaches.",
    "Low",
)
render_domain_workflow(
    "projection",
    [
        "Write a professional biography",
        "Improve a LinkedIn About section",
        "Create a conference-speaker introduction",
        "Draft a research collaboration message",
        "Prepare a fellowship profile",
        "Develop a clinician education content calendar",
        "Create a portfolio summary",
        "Write a grant-investigator profile",
        "Prepare a webinar introduction",
    ],
    [
        "Clinician-researcher profile",
        "Medical affairs leader biography",
        "Conference introduction",
        "Collaboration outreach",
        "Public education post",
    ],
    "an ethical healthcare communications and personal-branding strategist",
    """- Do not exaggerate credentials, roles, outcomes or expertise.
- Do not reveal confidential cases or patient stories without consent.
- Distinguish educational content from medical advice.
- Include conflict-of-interest disclosure where relevant.""",
    "Low",
)
