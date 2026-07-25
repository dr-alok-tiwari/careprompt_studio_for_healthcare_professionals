from components.layout import page_header
from components.domain_workflow import render_domain_workflow

page_header(
    "Pharma & Medical Affairs Studio",
    "Develop evidence-grounded, non-promotional scientific workflows with review points.",
    "High",
)
render_domain_workflow(
    "pharma",
    [
        "Prepare an MSL scientific briefing",
        "Summarise congress evidence",
        "Draft an advisory-board discussion guide",
        "Categorise field medical insights",
        "Create a medical-information response outline",
        "Develop an unmet-need assessment",
        "Prepare an HTA evidence checklist",
        "Create a publication plan",
        "Build a treatment-pathway analysis",
    ],
    [
        "Oncology congress update",
        "KOL discussion preparation",
        "Real-world evidence question",
        "Medical information enquiry",
        "Patient-support programme",
    ],
    "a medical affairs lead and evidence-communication specialist",
    """- Separate evidence, interpretation, assumptions and claims.
- Do not generate unsupported promotional claims.
- Mark content requiring medical, legal and regulatory review.
- Verify indication, population, endpoints and source context.
- Do not enter confidential company information into unapproved systems.""",
    "High",
)
