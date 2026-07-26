"""Generate the 500-item CarePrompt Learning Lab MCQ bank.

The bank combines 50 reviewed healthcare-AI concepts with 10 realistic
professional settings. Options are deterministically shuffled so the correct
answer does not remain in a predictable position.
"""

from __future__ import annotations

import json
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "quizzes.json"

CONTEXTS = [
    "Outpatient consultation — a clinician is preparing AI-assisted material",
    "Inpatient ward round — a multidisciplinary team is reviewing an AI-supported workflow",
    "Telemedicine encounter — a remote-care team is considering an AI-generated output",
    "Clinical research study — investigators are using AI during a study workflow",
    "Pharmacovigilance review — a safety team is assessing AI-assisted case work",
    "Medical-affairs evidence brief — a team is preparing scientific communication",
    "Patient-education session — staff are creating material for patients and caregivers",
    "Healthcare analytics project — analysts are developing a decision-support output",
    "Medical-imaging research workflow — researchers are evaluating an AI-supported process",
    "Quality-improvement meeting — leaders are deciding how to use AI responsibly",
]


def concept(
    topic: str,
    difficulty: str,
    question: str,
    answer: str,
    distractors: list[str],
    explanation: str,
) -> dict:
    return {
        "topic": topic,
        "difficulty": difficulty,
        "question": question,
        "answer": answer,
        "distractors": distractors,
        "explanation": explanation,
    }


CONCEPTS = [
    concept(
        "Privacy & governance",
        "Foundation",
        "What is the safest first step before entering a real case into a public AI tool?",
        "Minimise and de-identify the data, then confirm organisational approval",
        [
            "Enter the complete record so the model has maximum context",
            "Replace only the patient name and keep every other identifier",
            "Ask the model to promise that it will keep the information secret",
        ],
        "Safe use requires data minimisation, meaningful de-identification and approval of the tool and workflow.",
    ),
    concept(
        "Privacy & governance",
        "Foundation",
        "What does data minimisation require?",
        "Use only the least amount of information necessary for the defined task",
        [
            "Upload all available information in case it becomes useful later",
            "Remove clinical details but retain direct identifiers",
            "Keep the full dataset and hide it from the final output",
        ],
        "Data minimisation limits collection and disclosure to information necessary for a specified purpose.",
    ),
    concept(
        "Privacy & governance",
        "Intermediate",
        "A record has no name but contains a rare diagnosis, exact age and small location. What is the main concern?",
        "The combination may still permit re-identification",
        [
            "The record is automatically anonymous because the name is absent",
            "Rare diagnoses are never identifying",
            "Re-identification matters only when an image is uploaded",
        ],
        "Indirect identifiers can combine to make an individual recognisable even after direct identifiers are removed.",
    ),
    concept(
        "Privacy & governance",
        "Intermediate",
        "What is the best approach when consent may be required for an AI-enabled workflow?",
        "Confirm the lawful basis and document consent or another valid basis before use",
        [
            "Assume general treatment consent covers every future AI use",
            "Collect consent only after the output has been shared",
            "Let the AI system decide whether consent is needed",
        ],
        "Consent and other lawful bases must be determined prospectively under applicable policy and law.",
    ),
    concept(
        "Privacy & governance",
        "Advanced",
        "Which retention practice is most defensible for AI inputs and outputs?",
        "Define a purpose-based retention period and securely delete material when it is no longer needed",
        [
            "Retain every prompt indefinitely for possible future analysis",
            "Keep outputs forever but delete only the prompts",
            "Allow each user to choose an undocumented retention period",
        ],
        "Governed retention uses a documented purpose, access controls and secure disposal rather than indefinite storage.",
    ),
    concept(
        "Prompt engineering",
        "Foundation",
        "Which prompt structure most improves relevance for a healthcare task?",
        "State the context, role, audience, task, format and safety boundaries",
        [
            "Use a single vague instruction and let the model infer everything",
            "Add as many unrelated details as possible",
            "Ask for a confident answer without defining the audience",
        ],
        "Clear task framing and boundaries reduce ambiguity and make review easier.",
    ),
    concept(
        "Prompt engineering",
        "Foundation",
        "Why should a prompt include explicit constraints?",
        "Constraints define what the output must and must not do",
        [
            "Constraints guarantee that every factual claim is correct",
            "Constraints transfer accountability to the model",
            "Constraints make professional review unnecessary",
        ],
        "Constraints guide scope and behaviour, but they do not guarantee accuracy or replace review.",
    ),
    concept(
        "Prompt engineering",
        "Intermediate",
        "What is the benefit of specifying an output format?",
        "It makes the result easier to inspect, compare and use in the intended workflow",
        [
            "It proves that the underlying evidence is valid",
            "It prevents all hallucinations",
            "It allows sensitive information to be entered safely",
        ],
        "A defined structure supports usability and verification but does not validate the content itself.",
    ),
    concept(
        "Prompt engineering",
        "Intermediate",
        "What is the best response when the first AI output is incomplete?",
        "Identify the missing elements and iteratively refine the prompt while preserving safety limits",
        [
            "Accept the first output because regeneration introduces bias",
            "Remove all constraints so the model can improvise",
            "Ask for a longer answer without naming what is missing",
        ],
        "Targeted iteration is more useful than accepting an incomplete draft or merely increasing length.",
    ),
    concept(
        "Prompt engineering",
        "Advanced",
        "Which instruction best manages uncertainty?",
        "Separate known facts, assumptions, uncertainties and information that requires verification",
        [
            "Present the most likely interpretation as certain",
            "Remove caveats so the answer is easier to read",
            "Use confidence scores without explaining their basis",
        ],
        "Explicit uncertainty supports calibrated decision-making and focused human verification.",
    ),
    concept(
        "Evidence & citations",
        "Foundation",
        "How should an AI-generated citation be handled?",
        "Verify the source exists and that it supports the exact claim",
        [
            "Trust it if the journal title and DOI look plausible",
            "Use it when the model expresses high confidence",
            "Verify only the publication year",
        ],
        "AI can fabricate or misapply references; both bibliographic existence and claim-level support must be checked.",
    ),
    concept(
        "Evidence & citations",
        "Foundation",
        "A real paper is cited for a claim it does not support. What type of error is this?",
        "Citation misattribution",
        [
            "Data encryption",
            "Sampling stratification",
            "Model calibration",
        ],
        "A genuine source can still be cited inaccurately when its findings do not support the stated claim.",
    ),
    concept(
        "Evidence & citations",
        "Intermediate",
        "When evidence sources disagree, what is the most appropriate action?",
        "Compare study quality, population, methods, dates and applicability, then report the disagreement",
        [
            "Select the source with the most confident wording",
            "Average all conclusions without appraisal",
            "Hide the disagreement to avoid confusing the audience",
        ],
        "Evidence synthesis should explain heterogeneity and applicability rather than suppress conflicting findings.",
    ),
    concept(
        "Evidence & citations",
        "Intermediate",
        "Which source is generally most appropriate for a current drug-labelling claim?",
        "The applicable regulator-approved label or official product information",
        [
            "An unattributed social-media post",
            "A model-generated summary without links",
            "A promotional slide from an unknown date",
        ],
        "Regulator-approved product information is the primary reference for jurisdiction-specific labelling claims.",
    ),
    concept(
        "Evidence & citations",
        "Advanced",
        "Why should the date and jurisdiction of a guideline be recorded?",
        "Recommendations and applicability can change over time and across health systems",
        [
            "A dated guideline never needs critical appraisal",
            "Jurisdiction affects formatting but not clinical applicability",
            "Recording the date guarantees the guidance is current",
        ],
        "Guidelines reflect a particular evidence window, population, policy environment and care system.",
    ),
    concept(
        "Clinical safety",
        "Foundation",
        "Who remains accountable for a patient-facing AI-assisted output?",
        "The qualified professional and organisation using the output",
        [
            "The prompt template alone",
            "The model because it generated the wording",
            "No one when a disclaimer is displayed",
        ],
        "Professional and organisational accountability cannot be delegated to an AI system.",
    ),
    concept(
        "Clinical safety",
        "Foundation",
        "What should happen when an AI output may overlook a red flag?",
        "Pause use, obtain qualified review and follow the appropriate escalation pathway",
        [
            "Regenerate until the red flag disappears",
            "Use the output if most other details are correct",
            "Ask the patient to decide whether the red flag matters",
        ],
        "Potential red flags require human assessment and established escalation, not repeated generation.",
    ),
    concept(
        "Clinical safety",
        "Intermediate",
        "What is the safest use of AI for medication-dose information?",
        "Use it only as a draft or cross-check and verify against authoritative sources and patient-specific factors",
        [
            "Prescribe directly from the first generated dose",
            "Assume standard dosing applies to every patient",
            "Ignore renal, hepatic and interaction considerations",
        ],
        "Dosing is high risk and depends on verified sources, clinical context and qualified judgement.",
    ),
    concept(
        "Clinical safety",
        "Intermediate",
        "How should a possible emergency described during an AI-supported interaction be handled?",
        "Use the established emergency pathway immediately rather than waiting for AI interpretation",
        [
            "Ask the model for a definitive diagnosis first",
            "Continue routine prompting until certainty is achieved",
            "Schedule a non-urgent review without assessing urgency",
        ],
        "Emergency escalation must follow established clinical processes without delay.",
    ),
    concept(
        "Clinical safety",
        "Advanced",
        "What makes an educational differential diagnosis safer?",
        "It states uncertainty, identifies missing information and red flags, and requires qualified review",
        [
            "It ranks one diagnosis as certain without examination",
            "It automatically selects treatment",
            "It omits alternatives to reduce cognitive load",
        ],
        "A differential is decision support only when uncertainty, missing data and escalation needs remain explicit.",
    ),
    concept(
        "Patient communication",
        "Foundation",
        "Which wording principle best supports patient understanding?",
        "Use plain language, short explanations and define necessary medical terms",
        [
            "Use specialist terminology to demonstrate authority",
            "Include every technical detail regardless of relevance",
            "Avoid examples because they may simplify the topic",
        ],
        "Plain language improves accessibility while necessary clinical nuance can still be preserved.",
    ),
    concept(
        "Patient communication",
        "Foundation",
        "What is the purpose of teach-back?",
        "Ask the person to explain the information in their own words so understanding can be checked",
        [
            "Test whether the patient can memorise exact wording",
            "Make the patient responsible for communication errors",
            "Replace informed consent documentation",
        ],
        "Teach-back checks the clarity of communication and creates an opportunity to correct misunderstanding.",
    ),
    concept(
        "Patient communication",
        "Intermediate",
        "How should AI-translated medical information be used?",
        "Treat it as a draft and obtain qualified bilingual review for important communication",
        [
            "Assume fluent translation is clinically accurate",
            "Use it without review when the language is common",
            "Translate only the diagnosis and omit instructions",
        ],
        "Fluency does not ensure accurate medical meaning, cultural fit or safe instructions.",
    ),
    concept(
        "Patient communication",
        "Intermediate",
        "What is the best way to communicate clinical uncertainty?",
        "Explain what is known, what is uncertain, what will happen next and when to seek help",
        [
            "Hide uncertainty to maintain confidence",
            "List probabilities without context or next steps",
            "Use only a generic disclaimer at the end",
        ],
        "Transparent uncertainty paired with a plan supports trust and safer action.",
    ),
    concept(
        "Patient communication",
        "Advanced",
        "Which review best improves equity in patient-facing material?",
        "Check language, literacy, disability access, cultural context and practical barriers with target users",
        [
            "Use one standard version for every population",
            "Review only grammar and visual branding",
            "Assume digital access and health literacy are uniform",
        ],
        "Equitable communication considers diverse needs and tests material with intended users.",
    ),
    concept(
        "Research integrity",
        "Foundation",
        "What should an AI tool do when study data are missing?",
        "Flag the gap and avoid inventing values or results",
        [
            "Generate plausible values to complete the table",
            "Copy results from a similar study without disclosure",
            "Remove the variable and report the analysis as complete",
        ],
        "Fabricating data is research misconduct; missingness must be handled transparently and methodologically.",
    ),
    concept(
        "Research integrity",
        "Foundation",
        "How should a protocol deviation be handled?",
        "Document, justify and assess its effect according to the approved protocol and governance process",
        [
            "Hide it if the final result remains significant",
            "Rewrite the protocol after seeing the result without disclosure",
            "Ask the AI to describe it as planned",
        ],
        "Transparent documentation is necessary to assess bias, validity and compliance.",
    ),
    concept(
        "Research integrity",
        "Intermediate",
        "Which practice most improves computational reproducibility?",
        "Version code, record environments and seeds, and preserve a documented analysis pipeline",
        [
            "Keep only screenshots of final results",
            "Edit results manually after analysis",
            "Report the software name without versions or code",
        ],
        "Reproducibility depends on traceable data processing, code, parameters and environments.",
    ),
    concept(
        "Research integrity",
        "Intermediate",
        "How should AI use in manuscript preparation be reported?",
        "Follow journal policy and transparently disclose relevant use while retaining human responsibility",
        [
            "List the AI system as an author",
            "Never disclose AI assistance under any circumstances",
            "Let the model approve the final manuscript",
        ],
        "AI cannot meet authorship accountability; disclosure should follow applicable journal and institutional rules.",
    ),
    concept(
        "Research integrity",
        "Advanced",
        "What is the most defensible approach to authorship?",
        "Apply established contribution and accountability criteria independently of tool use",
        [
            "Grant authorship to anyone who supplied an AI prompt",
            "Let the corresponding author decide without discussion",
            "Use author order as compensation for data access",
        ],
        "Authorship requires substantive contributions, approval and accountability under accepted criteria.",
    ),
    concept(
        "Bias & fairness",
        "Foundation",
        "Why should model performance be reported for relevant subgroups?",
        "Overall performance can hide clinically important disparities",
        [
            "Subgroup analysis always increases overall accuracy",
            "A large sample guarantees equal performance",
            "Fairness can be inferred from the model architecture",
        ],
        "Aggregate metrics may conceal poor performance for particular populations or settings.",
    ),
    concept(
        "Bias & fairness",
        "Foundation",
        "What is a key risk of non-representative training data?",
        "The model may generalise poorly to under-represented populations",
        [
            "The model will automatically correct population imbalance",
            "Representation affects speed but not validity",
            "Only the user interface will be biased",
        ],
        "Training distributions influence where a model performs reliably and where errors may concentrate.",
    ),
    concept(
        "Bias & fairness",
        "Intermediate",
        "Why can a seemingly neutral variable create unfairness?",
        "It may act as a proxy for a protected or structurally disadvantaged characteristic",
        [
            "Neutral variables cannot correlate with social conditions",
            "Proxy effects occur only in image data",
            "Removing labels eliminates every form of bias",
        ],
        "Variables such as geography or utilisation can encode structural inequities and protected characteristics.",
    ),
    concept(
        "Bias & fairness",
        "Intermediate",
        "What does calibration assess?",
        "Whether predicted probabilities correspond to observed outcome frequencies",
        [
            "Whether the interface uses balanced colours",
            "Whether every subgroup has the same sample size",
            "Whether the model explains causal mechanisms",
        ],
        "A calibrated risk estimate of 20% should correspond to an outcome rate near 20% in comparable cases.",
    ),
    concept(
        "Bias & fairness",
        "Advanced",
        "Why is post-deployment drift monitoring necessary?",
        "Populations, workflows, measurements and clinical practice can change after validation",
        [
            "A validated model cannot lose performance",
            "Drift matters only when the software version changes",
            "Monitoring is unnecessary if users like the tool",
        ],
        "Real-world distributions and processes evolve, so safety and equity require ongoing measurement.",
    ),
    concept(
        "Data & statistics",
        "Foundation",
        "What is data leakage?",
        "Information unavailable at the intended prediction time improperly influences model development",
        [
            "Missing values are deleted before analysis",
            "A dataset is encrypted during transfer",
            "A model is evaluated on a protected subgroup",
        ],
        "Leakage produces overly optimistic performance because the model accesses future or otherwise unavailable information.",
    ),
    concept(
        "Data & statistics",
        "Foundation",
        "How should missing data be handled?",
        "Examine the pattern and mechanism, justify the method and assess sensitivity",
        [
            "Replace every missing value with zero",
            "Delete incomplete records without reporting it",
            "Ask an AI model to invent realistic values",
        ],
        "Missing-data handling should reflect its mechanism and potential effect on bias and precision.",
    ),
    concept(
        "Data & statistics",
        "Intermediate",
        "Why is external validation important?",
        "It tests performance in data that differ meaningfully from the development sample",
        [
            "It guarantees approval in every jurisdiction",
            "It replaces the need for internal validation",
            "It is identical to testing on a random split from the same dataset",
        ],
        "External validation assesses transportability across settings, times or populations.",
    ),
    concept(
        "Data & statistics",
        "Intermediate",
        "For a rare harmful outcome, why can accuracy be misleading?",
        "A model can predict the majority class and appear accurate while missing most true cases",
        [
            "Accuracy always equals sensitivity",
            "Rare outcomes eliminate false positives",
            "Class imbalance affects training speed only",
        ],
        "Imbalanced outcomes require metrics such as sensitivity, specificity, precision, recall and calibration.",
    ),
    concept(
        "Data & statistics",
        "Advanced",
        "What is the main concern when many hypotheses are tested without adjustment or pre-specification?",
        "The chance of false-positive findings increases",
        [
            "Statistical power always becomes zero",
            "Every significant result becomes causal",
            "Confidence intervals become unnecessary",
        ],
        "Multiple testing raises the probability of chance findings and requires transparent control or interpretation.",
    ),
    concept(
        "Pharmacovigilance & medical affairs",
        "Foundation",
        "Which elements make a report a potentially valid individual adverse-event case?",
        "An identifiable reporter, identifiable patient, suspected product and adverse event",
        [
            "A product name and marketing slogan only",
            "A literature title without a patient or event",
            "A reporter opinion without a suspected product",
        ],
        "The four minimum elements support recognition and processing of a potential individual case.",
    ),
    concept(
        "Pharmacovigilance & medical affairs",
        "Foundation",
        "How do seriousness and severity differ?",
        "Seriousness is based on regulatory outcome criteria; severity describes intensity",
        [
            "They are interchangeable terms",
            "Severity depends only on the product dose",
            "Seriousness means the event was unexpected",
        ],
        "A severe event is not necessarily serious, and a serious event may not be described as severe.",
    ),
    concept(
        "Pharmacovigilance & medical affairs",
        "Intermediate",
        "How should an AI-generated causality assessment be used?",
        "As structured support only, with qualified review using complete case information",
        [
            "As the final regulatory determination",
            "As proof that the product caused the event",
            "Without considering alternative causes or timing",
        ],
        "Causality assessment requires clinical and regulatory judgement, chronology and alternative explanations.",
    ),
    concept(
        "Pharmacovigilance & medical affairs",
        "Intermediate",
        "What makes a medical-affairs evidence brief appropriately balanced?",
        "It separates evidence, interpretation and limitations and represents relevant favourable and unfavourable findings",
        [
            "It includes only findings that support the desired message",
            "It converts every association into a causal claim",
            "It removes limitations to make the document concise",
        ],
        "Balanced scientific communication avoids selective presentation and unsupported promotional inference.",
    ),
    concept(
        "Pharmacovigilance & medical affairs",
        "Advanced",
        "What should happen if an adverse event appears during a non-safety AI workflow?",
        "Route it promptly through the approved pharmacovigilance reporting process",
        [
            "Ignore it because the workflow was not designed for safety",
            "Wait for the AI system to confirm causality",
            "Remove the event from the text and continue",
        ],
        "Potential safety information must be escalated according to reporting obligations regardless of where it appears.",
    ),
    concept(
        "Implementation & security",
        "Foundation",
        "What is the safest way to introduce a new AI workflow?",
        "Start with a scoped pilot, defined success and safety measures, and human oversight",
        [
            "Deploy organisation-wide before defining outcomes",
            "Measure only user enthusiasm",
            "Allow each user to invent a separate ungoverned process",
        ],
        "A controlled pilot supports learning, risk detection and evidence-based scale-up.",
    ),
    concept(
        "Implementation & security",
        "Foundation",
        "Why are audit logs useful?",
        "They support traceability of access, changes, decisions and incidents",
        [
            "They make authentication unnecessary",
            "They prove every output is clinically correct",
            "They should contain unrestricted copies of all sensitive data",
        ],
        "Proportionate audit trails help investigate use and incidents while still requiring privacy controls.",
    ),
    concept(
        "Implementation & security",
        "Intermediate",
        "Which control most directly reduces unauthorised access?",
        "Role-based access, strong authentication and least-privilege permissions",
        [
            "A general disclaimer on the home page",
            "A shared password for the whole team",
            "Public links that expire only when manually removed",
        ],
        "Identity, authentication and least privilege are core safeguards for controlled access.",
    ),
    concept(
        "Implementation & security",
        "Intermediate",
        "Why should model and prompt versions be recorded?",
        "Outputs and risks can change when models, prompts, data or settings change",
        [
            "Versioning prevents every future error",
            "Only the visual theme affects reproducibility",
            "Model updates never affect validated workflows",
        ],
        "Version records make changes traceable and support revalidation, incident review and reproducibility.",
    ),
    concept(
        "Implementation & security",
        "Advanced",
        "What should a healthcare AI procurement review include?",
        "Clinical fit, evidence, privacy, security, integration, accessibility, cost, monitoring and exit arrangements",
        [
            "Only the vendor demonstration and purchase price",
            "Only the model's benchmark score",
            "Only whether the product name includes AI",
        ],
        "Safe procurement evaluates the full sociotechnical lifecycle, not only performance or price.",
    ),
]


def build_bank() -> list[dict]:
    bank: list[dict] = []
    for concept_index, item in enumerate(CONCEPTS):
        for context_index, context in enumerate(CONTEXTS):
            options = [item["answer"], *item["distractors"]]
            random.Random(concept_index * 100 + context_index).shuffle(options)
            sequence = len(bank) + 1
            bank.append(
                {
                    "id": f"CPQ-{sequence:03d}",
                    "topic": item["topic"],
                    "difficulty": item["difficulty"],
                    "context": context.split(" — ", 1)[0],
                    "question": f"{context}. {item['question']}",
                    "options": options,
                    "answer": item["answer"],
                    "explanation": item["explanation"],
                }
            )
    return bank


def main() -> None:
    bank = build_bank()
    if len(bank) != 500:
        raise RuntimeError(f"Expected 500 questions, generated {len(bank)}")
    OUTPUT.write_text(
        json.dumps(bank, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
