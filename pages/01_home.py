import streamlit as st

from components.layout import metric_card, page_header, safe_callout, step_card
from services.tool_registry import load_tools
from utils.helpers import load_json

page_header(
    "CarePrompt Studio",
    "A guided, no-API-first workbench for patient-centred communication, clinical reasoning education, research, pharma workflows and professional visibility.",
)

templates = load_json("prompt_templates.json")
tools = load_tools()

c1, c2, c3, c4 = st.columns(4)
with c1:
    metric_card("Prompt templates", str(len(templates)), "Editable and safety-aware")
with c2:
    metric_card("AI tools", str(len(tools)), "Free options prioritised")
with c3:
    metric_card("Guided cases", "18", "Fictional progressive scenarios")
with c4:
    metric_card("Default mode", "No API", "Works without a paid key")

safe_callout(
    "Designed for busy healthcare professionals",
    "Every major input now offers an editable sample, a manual-entry option and prompt nudges. You remain in control of the final wording.",
)

st.subheader("Choose your starting point")

cards = [
    (
        "🤝 Patient-centred communication",
        "Create plain-language explanations, counselling scripts, journey maps and teach-back questions.",
        "pages/03_patient_centricity.py",
        "Open Patient-Centricity Studio",
    ),
    (
        "🩺 Clinical reasoning education",
        "Structure missing information, differentials, red flags and referral questions without autonomous diagnosis.",
        "pages/04_clinical_reasoning.py",
        "Open Clinical Reasoning",
    ),
    (
        "🔬 Research and evidence",
        "Move from idea to search strategy, design, analysis, reporting and reviewer response.",
        "pages/05_research_studio.py",
        "Open Research Studio",
    ),
    (
        "💊 Pharma and medical affairs",
        "Prepare evidence briefs, congress summaries, advisory-board guides and non-promotional medical content.",
        "pages/06_pharma_medical_affairs.py",
        "Open Medical Affairs Studio",
    ),
    (
        "✨ Universal prompt builder",
        "Build a CRAFT-MED prompt with examples, custom constraints, evidence checks and human-review safeguards.",
        "pages/09_prompt_builder.py",
        "Open Prompt Builder",
    ),
    (
        "🧰 AI tool selection",
        "Compare free, freemium, open-source and paid tools with privacy and citation considerations.",
        "pages/10_ai_tool_directory.py",
        "Open AI Tool Directory",
    ),
]

for row_start in range(0, len(cards), 3):
    columns = st.columns(3)
    for column, (title, body, page, label) in zip(columns, cards[row_start : row_start + 3]):
        with column:
            st.markdown(
                f'<div class="cp-card"><h3>{title}</h3><p>{body}</p></div>',
                unsafe_allow_html=True,
            )
            st.page_link(page, label=label, use_container_width=True)

st.subheader("A simple three-step workflow")
step_card(1, "Start with a sample or type manually", "Choose an editable fictional example to overcome the blank page, or enter your own de-identified context.")
step_card(2, "Add constraints and nudges", "Specify the audience, format, tone, evidence standard, safety boundaries and review requirements.")
step_card(3, "Generate, verify and save", "Copy the ChatGPT-ready prompt, verify critical content, and save a reviewed version in your session workspace.")

with st.expander("60-second guided tour", expanded=False):
    st.markdown(
        "1. Complete **Get Started** to personalise the app.\n"
        "2. Open a relevant work studio.\n"
        "3. Select a quick-start example or type your own de-identified context.\n"
        "4. Add prompt nudges and a required reviewer.\n"
        "5. Generate the prompt and inspect the privacy warning.\n"
        "6. Copy, download or save it to **My Workspace**.\n"
        "7. Compare specialised tools in **AI Tool Directory**."
    )

st.info("Recommended first action: complete **Get Started**, then use the **Universal Prompt Builder** for a real, non-sensitive task.")
