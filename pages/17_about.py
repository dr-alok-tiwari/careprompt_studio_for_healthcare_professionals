import streamlit as st
from components.layout import page_header
from config.app_config import (
    APP_VERSION,
    DEVELOPER_NAME,
    DEVELOPER_ROLE,
    DEVELOPER_ORG,
    PORTFOLIO_URL,
    GITHUB_URL,
)

page_header(
    "About CarePrompt Studio",
    "A responsible, no-API-first healthcare prompt and AI-tool learning environment.",
)
st.markdown(
    f"""
### Value proposition
CarePrompt Studio helps healthcare professionals convert real work needs into structured prompts, compare specialised tools and apply privacy, evidence and human-review safeguards.

### Developer
**{DEVELOPER_NAME}**  
{DEVELOPER_ROLE}  
{DEVELOPER_ORG}
"""
)
c1, c2 = st.columns(2)
c1.link_button("Portfolio", PORTFOLIO_URL)
c2.link_button("GitHub", GITHUB_URL)

st.subheader("Alternative name concepts")
st.write(
    "CarePrompt Studio · PatientFirst AI Lab · Clinician PromptWorks · MedCentric AI Studio · "
    "CareCraft AI · HealthPrompt Compass · EvidenceCare Studio · ClinAI Workbench · PatientVoice AI · MedProfessional Copilot"
)

st.subheader("Limitations")
st.markdown(
    """- Not a medical device or validated clinical decision-support system.
- The local privacy checker detects only selected patterns.
- Tool pricing, features and availability can change.
- AI outputs can be incomplete, biased or inaccurate.
- Organisational deployment requires local legal, privacy, security and governance review."""
)
st.caption(f"Version {APP_VERSION}")
