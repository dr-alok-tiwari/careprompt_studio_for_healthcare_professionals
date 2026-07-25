from dataclasses import dataclass


@dataclass
class PromptInputs:
    context: str
    role: str
    audience: str
    format: str
    task: str
    safeguards: str
    evidence: str
    details: str


def build_craft_med(data: PromptInputs) -> str:
    return f"""You are acting as: {data.role}.

CONTEXT
{data.context}

TASK
{data.task}

AUDIENCE
{data.audience}

REQUIRED FORMAT
{data.format}

MEDICAL, ETHICAL AND PRIVACY SAFEGUARDS
{data.safeguards}
- Use only fictional or de-identified information.
- Clearly distinguish facts, assumptions, uncertainties and recommendations.
- Do not fabricate citations, guidelines, statistics or clinical findings.
- Do not replace qualified clinical, medical, legal, regulatory or statistical review.

EVIDENCE REQUIREMENTS
{data.evidence}

DETAILS AND CONSTRAINTS
{data.details}

QUALITY CONTROL BEFORE FINALISING
1. Identify any missing information that materially affects the answer.
2. State uncertainty and limitations explicitly.
3. Check whether any claim requires verification.
4. Add a short human-review checklist.
5. End with the safest next professional action, without presenting the output as autonomous medical advice."""


def evaluate_prompt(prompt: str) -> dict[str, int]:
    p = prompt.lower()
    checks = {
        "Task clarity": ["task", "create", "draft", "analyse", "explain"],
        "Context sufficiency": ["context", "background", "situation"],
        "Audience specification": ["audience", "patient", "clinician", "researcher", "professional"],
        "Output format": ["format", "table", "bullet", "report", "script"],
        "Evidence requirements": ["evidence", "citation", "guideline", "source"],
        "Safety constraints": ["safety", "do not", "human review", "not a diagnosis"],
        "Privacy protection": ["de-ident", "privacy", "confidential", "identifiable"],
        "Uncertainty handling": ["uncertainty", "limitations", "assumptions"],
        "Verification": ["verify", "verification", "check"],
        "Actionability": ["checklist", "next", "steps", "action"],
    }
    return {key: min(10, 2 * sum(1 for term in terms if term in p)) for key, terms in checks.items()}


def improve_prompt(prompt: str) -> str:
    additions: list[str] = []
    low = prompt.lower()
    if "audience" not in low:
        additions.append("Define the intended audience and its health-literacy or expertise level.")
    if "format" not in low:
        additions.append("Specify the required output format, length and tone.")
    if "do not fabricate" not in low:
        additions.append("Do not fabricate references, guidelines, data or clinical findings.")
    if "uncertainty" not in low:
        additions.append("State uncertainty, assumptions and missing information explicitly.")
    if "human review" not in low:
        additions.append("Add a qualified human-review checklist before use.")
    requirements = additions or ["Retain the existing safeguards and verify all factual claims."]
    return prompt.rstrip() + "\n\nADDITIONAL QUALITY REQUIREMENTS\n- " + "\n- ".join(requirements)
