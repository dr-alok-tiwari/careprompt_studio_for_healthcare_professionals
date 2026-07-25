from services.tool_registry import load_tools


def recommend(task: str, free_required: bool, citations: bool, sensitive: bool, technical: str) -> list[dict]:
    df = load_tools()
    task_lower = task.lower()
    category_map = {
        "research": "Research discovery",
        "literature": "Research discovery",
        "presentation": "Presentation",
        "statistics": "Data & statistics",
        "data": "Data & statistics",
        "patient": "Patient communication",
        "clinical": "Clinical evidence",
        "citation": "Reference management",
        "write": "Academic writing",
    }
    category = next((v for k,v in category_map.items() if k in task_lower), "General AI")
    cand = df[df["category"].isin([category, "General AI"])]
    if free_required:
        cand = cand[cand["access"].isin(["Free", "Freemium", "Open source"])]
    if sensitive:
        cand = cand[cand["patient_data"] == "Do not enter"]
    if citations:
        cand = cand.sort_values(by="citation_support", ascending=False)
    if technical == "Beginner":
        cand = cand.sort_values(by="ease", ascending=False)
    rows = cand.head(5).to_dict("records")
    return rows
