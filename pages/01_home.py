import streamlit as st
from components.layout import page_header, metric_card
from components.cards import action_card
from utils.helpers import load_json
from services.tool_registry import load_tools

page_header("CarePrompt Studio", "A no-API-first AI workbench for patient-centred healthcare, research, pharma workflows and professional communication.")
templates = load_json("prompt_templates.json")
tools = load_tools()
c1,c2,c3,c4 = st.columns(4)
with c1: metric_card("Prompt templates", str(len(templates)), "Customisable and safety-aware")
with c2: metric_card("AI tools", str(len(tools)), "Free options prioritised")
with c3: metric_card("Learning cases", "18", "Fictional, progressive scenarios")
with c4: metric_card("Default mode", "No API", "Works without a paid key")

st.subheader("What would you like to accomplish today?")
cols = st.columns(3)
items = [
    ("Improve patient communication", "Build plain-language counselling and follow-up prompts.", "Patient-first"),
    ("Structure clinical reasoning", "Create an educational differential-reasoning prompt with red flags.", "Human review"),
    ("Plan a research study", "Move from idea to question, design, analysis and writing prompts.", "Evidence-aware"),
    ("Prepare medical affairs content", "Create a scientific brief with MLR review points.", "Non-promotional"),
    ("Strengthen professional projection", "Develop an ethical profile, presentation or collaboration message.", "Authentic"),
    ("Choose an AI tool", "Compare free, freemium, paid and open-source alternatives.", "Decision support"),
]
for i,item in enumerate(items):
    with cols[i%3]: action_card(*item)

with st.expander("60-second guided tour"):
    st.markdown("1. Complete **Get Started**. 2. Open a work studio. 3. Add de-identified context. 4. Apply prompt nudges. 5. Review safety flags. 6. Copy or save the prompt. 7. Compare specialised tools in the directory.")

st.info("Recommended starting point: complete **Get Started**, then use **Prompt Builder** for a task that matters to you.")
