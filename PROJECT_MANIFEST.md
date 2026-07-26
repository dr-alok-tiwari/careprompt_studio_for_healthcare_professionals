# CarePrompt Studio — Project Manifest

## Build summary
- 17 Streamlit pages
- 180 prompt templates across 15 categories
- 77 AI and evidence tools with complete category-by-access coverage
- 18 fictional progressive cases
- 10 synthetic workshop datasets plus field-level data dictionary
- 500 explained quiz questions and 6 micro-lessons
- Local privacy pattern checker
- CRAFT-MED prompt engine and 10-dimension scorecard
- DOCX, PDF, Markdown, CSV and JSON exports
- Docker, Community Cloud, GitHub Actions and local setup files

## Validation performed
- Python bytecode compilation across the project
- Unit tests for prompt generation, safety redaction, tools, templates and exports
- Runtime-stub execution of all 17 Streamlit pages
- Tool-directory validation across all 40 category-by-access combinations
- Quiz validation for count, uniqueness, schema, balance and answer positions
- Streamlit startup health check
- Final result: 13 tests passed

## Runtime note
The app compiled, all tests passed and the Streamlit health endpoint returned `ok` in the validation environment.
