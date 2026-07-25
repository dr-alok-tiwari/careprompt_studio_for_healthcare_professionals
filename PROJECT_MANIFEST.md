# CarePrompt Studio — Project Manifest

## Build summary
- 17 Streamlit pages
- 180 prompt templates across 15 categories
- 56 AI and evidence tools
- 18 fictional progressive cases
- 10 synthetic workshop datasets plus field-level data dictionary
- 10 quiz questions and 6 micro-lessons
- Local privacy pattern checker
- CRAFT-MED prompt engine and 10-dimension scorecard
- DOCX, PDF, Markdown, CSV and JSON exports
- Docker, Community Cloud, GitHub Actions and local setup files

## Validation performed
- Python bytecode compilation across the project
- Unit tests for prompt generation, safety redaction, tools, templates and exports
- Runtime-stub execution of all 17 Streamlit pages
- Final result: 9 tests passed

## Runtime note
The build environment did not expose a Streamlit package index, so a live browser server could not be launched here. The project includes dependency pins, a Dockerfile and page-level runtime smoke tests for local execution.
