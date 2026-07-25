from components.layout import page_header
from components.domain_workflow import render_domain_workflow

page_header(
    "Clinical Reasoning Support",
    "Educational reasoning support—not an autonomous diagnostic system.",
    "High",
)
render_domain_workflow(
    "clinical",
    [
        "Generate a prioritised differential for educational review",
        "Structure a clinical history summary",
        "Identify missing clinical information",
        "Create a red-flag checklist",
        "Prepare a referral question",
        "Build a test-selection discussion",
        "Communicate diagnostic uncertainty",
        "Prepare a case presentation",
    ],
    [
        "Chest discomfort",
        "Persistent headache",
        "Fever with rash",
        "Anaemia",
        "Possible adverse drug reaction",
        "Abdominal pain",
        "Neurological symptoms",
    ],
    "a senior clinician supporting educational reasoning",
    """- Do not provide a final diagnosis.
- Do not prescribe, alter doses or advise stopping medicines.
- Explain supporting and opposing evidence.
- Identify missing information and emergency red flags.
- State uncertainty and recommend qualified clinical evaluation.""",
    "High",
)
