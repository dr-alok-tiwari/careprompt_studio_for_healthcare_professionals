# CarePrompt Studio

**CarePrompt Studio 2.0** is a modular, no-API-first Streamlit application for doctors, pharma professionals, researchers and healthcare managers. It helps users build responsible ChatGPT prompts, compare AI tools, practise fictional cases and apply privacy, evidence and human-review safeguards.

## What is new in version 2.0

- Redesigned accessible healthcare interface with navy, teal, mint and amber visual hierarchy
- Guided examples beside major text inputs
- Every sample remains fully editable; users can always type manually
- Custom audience, output format, tone, role and constraints
- Domain-specific prompt nudges for patient communication, clinical reasoning, research, medical affairs, pharmacovigilance and professional projection
- Editable sample patient journeys
- Guided onboarding, case practice, tool search, privacy checks and facilitator goals
- Complete category-by-access tool coverage with official links and indicative INR costs
- A filterable 500-MCQ Learning Lab with answer-reveal buttons and explanations
- Stronger review reminders and duplicate-safe workspace saving
- Automated GitHub checks for compilation, tests and Streamlit startup

## Core features

- 17 pages using `st.Page` and `st.navigation`
- 180 prompt templates
- 77 AI and evidence tools with access type, privacy notes, INR costs and official URLs
- Patient-centricity, clinical reasoning, research, medical affairs, pharmacovigilance and professional-projection studios
- Local privacy pattern checker
- Fictional cases, 500 explained MCQs and 10 synthetic datasets
- Session workspace with Markdown, JSON, DOCX and PDF export
- Facilitator agendas for 30 minutes to a full day
- Works without a paid API

## Local installation

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

## Run quality checks locally

```bash
python -m compileall -q app.py components config pages services utils
pytest -q
```

For a startup smoke test:

```bash
streamlit run app.py --server.headless=true --server.port=8501
```

Then open `http://localhost:8501/_stcore/health`. A healthy app returns `ok`.

## Streamlit Community Cloud deployment

1. Sign in to Streamlit Community Cloud.
2. Select repository `dr-alok-tiwari/careprompt_studio_for_healthcare_professionals`.
3. Select branch `main`.
4. Set the entry point to `app.py`.
5. Deploy or reboot the app.
6. In **App settings → General**, confirm Python 3.11 or 3.12 when selectable.
7. In **Manage app → Logs**, confirm that dependency installation completes and the health check succeeds.

The included `requirements.txt` and `.streamlit/config.toml` are detected automatically.

### Common Streamlit deployment fixes

- **`ModuleNotFoundError`**: confirm the missing package is listed in `requirements.txt`, then reboot the app.
- **Page or navigation errors**: ensure Streamlit 1.37 or newer is installed; this project uses `st.Page` and `st.navigation`.
- **Data file not found**: deploy from the repository root and use `app.py` as the entry point.
- **Stale UI after a merge**: reboot the app or clear the app cache from Streamlit Community Cloud.
- **App sleeps or shows a wake screen**: this is normal for inactive Community Cloud apps; wake or reboot it.
- **Dependency build failure**: use Python 3.11 or 3.12 and review the first package error in the deployment logs.

Add the final live app URL here after deployment:

```text
https://<your-careprompt-subdomain>.streamlit.app
```

## Docker

```bash
docker build -t careprompt-studio .
docker run --rm -p 8501:8501 careprompt-studio
```

Open `http://localhost:8501`.

## Customisation

- Branding and version: `config/app_config.py`
- Visual design: `config/theme.py` and `.streamlit/config.toml`
- Guided input controls: `components/guided_inputs.py`
- Prompt library: `data/prompt_templates.json`
- Tool directory: `data/tool_directory.csv`
- Cases and quizzes: `data/*.json`
- Synthetic data: `data/synthetic/`

## Privacy and safety

Do not enter identifiable patient, reporter or confidential organisational information. This is not a medical device and does not provide autonomous diagnosis, prescribing, dosing, emergency advice, pharmacovigilance submission or regulatory approval. Every high-risk output requires qualified human review.

The local pattern checker is only a preliminary aid. It does not guarantee anonymisation or compliance with institutional, legal or regulatory requirements.

## Troubleshooting checklist

- Run the app from the repository root.
- Use Python 3.11 or 3.12 for broad package compatibility.
- Recreate the virtual environment after major dependency changes.
- Review GitHub Actions before merging changes into `main`.
- Review Streamlit Community Cloud logs after every deployment.
- If PDF or DOCX export packages are unavailable, use Markdown export as a fallback.

## Developer

**Dr. Alok Tiwari**  
Assistant Professor – Big Data Analytics  
Goa Institute of Management

- Portfolio: https://dr-alok-tiwari.github.io/
- Repository: https://github.com/dr-alok-tiwari/careprompt_studio_for_healthcare_professionals
