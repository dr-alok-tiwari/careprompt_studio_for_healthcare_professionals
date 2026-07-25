import streamlit as st

from components.guided_inputs import guided_text_area, starter_for_domain
from components.layout import page_header, safe_callout
from services.recommendation_engine import recommend
from services.tool_registry import filter_tools, load_tools

page_header(
    "AI Tool Directory",
    "Compare free, freemium, paid and open-source tools. Pricing, features and availability can change—verify before adoption.",
)

df = load_tools()
tab1, tab2 = st.tabs(["🔎 Browse tools", "🧭 Get a recommendation"])

with tab1:
    safe_callout(
        "Search freely or use a quick nudge",
        "The quick-search selector fills the editable search field below. You can replace it with any tool, task or feature.",
    )

    quick_options = [
        "Type manually",
        "free literature review",
        "citation verification",
        "patient communication",
        "medical presentation",
        "data analysis",
        "reference management",
        "clinical evidence",
        "open source",
    ]
    quick = st.selectbox("Quick search nudge", quick_options, key="tool_quick_search")
    if "tool_search_text" not in st.session_state:
        st.session_state["tool_search_text"] = ""
    if quick != "Type manually" and st.session_state.get("tool_search_applied") != quick:
        st.session_state["tool_search_text"] = quick
        st.session_state["tool_search_applied"] = quick

    c1, c2, c3 = st.columns([2, 1, 1])
    with c1:
        query = st.text_input(
            "Search by tool, task or feature",
            key="tool_search_text",
            placeholder="Example: free evidence synthesis with citations",
        )
    with c2:
        category = st.selectbox("Category", ["All"] + sorted(df.category.unique().tolist()), key="tool_category")
    with c3:
        access = st.selectbox("Access", ["All"] + sorted(df.access.unique().tolist()), key="tool_access")

    out = filter_tools(query, category, access)
    st.caption(f"{len(out)} matching tools · Always review the last-verified field and official website")

    display_columns = [
        "tool",
        "category",
        "access",
        "best_for",
        "patient_data",
        "citation_support",
        "ease",
        "last_verified",
    ]
    st.dataframe(
        out[display_columns],
        use_container_width=True,
        hide_index=True,
        height=540,
        column_config={
            "tool": "Tool",
            "category": "Category",
            "access": "Access",
            "best_for": "Best for",
            "patient_data": "Patient-data guidance",
            "citation_support": "Citation support",
            "ease": "Ease",
            "last_verified": "Last verified",
        },
    )
    st.download_button(
        "Download complete directory CSV",
        df.to_csv(index=False).encode("utf-8"),
        "careprompt_tool_directory.csv",
        "text/csv",
        use_container_width=True,
    )

with tab2:
    safe_callout(
        "Recommendation logic",
        "Describe the task, then set your constraints. The result is decision support—not an endorsement or institutional approval.",
    )
    task = guided_text_area(
        "Describe the task",
        key="tool_recommendation_task",
        samples=starter_for_domain("tool"),
        placeholder="Type the task, desired output, evidence needs and privacy constraints.",
        height=155,
    )

    c1, c2 = st.columns(2)
    with c1:
        free = st.checkbox("Free access is mandatory", value=True, key="tool_free")
        citations = st.checkbox("Citation traceability is essential", value=True, key="tool_citations")
        collaboration = st.checkbox("Collaboration or sharing is required", value=False, key="tool_collaboration")
    with c2:
        sensitive = st.checkbox("Sensitive data may be involved", value=False, key="tool_sensitive")
        technical = st.radio("User comfort", ["Beginner", "Advanced"], horizontal=True, key="tool_technical")
        local_needed = st.checkbox("Local or self-hosted deployment is preferred", value=False, key="tool_local")

    custom_constraint = st.text_input(
        "Additional manual constraint",
        key="tool_custom_constraint",
        placeholder="Example: must export to DOCX and work without a credit card",
    )

    if st.button("Recommend tools", type="primary", use_container_width=True):
        full_task = task
        if collaboration:
            full_task += " Collaboration and sharing are required."
        if local_needed:
            full_task += " Prefer local or self-hosted tools."
        if custom_constraint.strip():
            full_task += f" Additional constraint: {custom_constraint.strip()}"

        if sensitive:
            st.warning(
                "Use only institutionally approved systems. De-identification alone may not satisfy local policy, consent or regulatory requirements."
            )

        rows = recommend(full_task, free, citations, sensitive, technical)
        if not rows:
            st.info("No exact match under the selected constraints. Relax one filter or consult your approved organisational tool list.")
        else:
            st.markdown("#### Recommended shortlist")
            for rank, row in enumerate(rows, start=1):
                with st.expander(f"#{rank} · {row['tool']} · {row['access']}", expanded=rank <= 2):
                    st.markdown(f"**Best for:** {row['best_for']}")
                    st.caption("Limitation: " + row["limitations"])
                    st.write(
                        "Patient data: **"
                        + row["patient_data"]
                        + "**  |  Citation support: **"
                        + row["citation_support"]
                        + "**  |  Ease: **"
                        + row["ease"]
                        + "**"
                    )
                    if row.get("official_url"):
                        st.link_button("Open official website", row["official_url"])

            st.info(
                "Before adoption, verify current pricing, regional access, privacy terms, data retention, export options and institutional approval."
            )
