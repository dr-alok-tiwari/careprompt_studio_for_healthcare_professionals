# CarePrompt Studio

A modular, no-API-first Streamlit application for doctors, pharma professionals, researchers and healthcare managers. It helps users build responsible ChatGPT prompts, compare AI tools, practise fictional cases and apply privacy/evidence safeguards.

## Key features
- 17 pages using `st.Page` and `st.navigation`
- 180 prompt templates
- 50+ AI tools with access type, privacy notes and official URLs
- Patient-centricity, clinical reasoning, research, medical affairs, pharmacovigilance and professional-projection studios
- Local privacy pattern checker
- Fictional cases, quizzes and 10 synthetic datasets
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

## Streamlit Community Cloud
1. Push this project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Select the repository, branch and `app.py`.
4. Deploy. The included `requirements.txt` and `.streamlit/config.toml` are detected automatically.

## Docker
```bash
docker build -t careprompt-studio .
docker run --rm -p 8501:8501 careprompt-studio
```
Open `http://localhost:8501`.

## Customisation
- Branding: `config/app_config.py` and `config/theme.py`
- Prompt library: `data/prompt_templates.json`
- Tool directory: `data/tool_directory.csv`
- Cases and quizzes: `data/*.json`
- Synthetic data: `data/synthetic/`

## Privacy and safety
Do not enter identifiable patient, reporter or confidential organisational information. This is not a medical device and does not provide autonomous diagnosis, prescribing, dosing, emergency advice, pharmacovigilance submission or regulatory approval. Every high-risk output requires qualified human review.

## Troubleshooting
- Run from the project root so relative data paths resolve.
- Use Python 3.11 or 3.12 for the broadest package compatibility.
- If PDF/DOCX packages are unavailable, the export service falls back to text output.
- If Streamlit reports an import error, recreate the virtual environment and reinstall requirements.
