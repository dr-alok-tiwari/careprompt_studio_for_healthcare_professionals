import streamlit as st
from components.layout import page_header
from services.tool_registry import load_tools, filter_tools
from services.recommendation_engine import recommend

page_header("AI Tool Directory", "Compare free, freemium, paid and open-source tools. Pricing and availability can change; verify before adoption.")
df = load_tools()
tab1,tab2 = st.tabs(["Browse tools", "Get a recommendation"])
with tab1:
    c1,c2,c3 = st.columns(3)
    with c1: query = st.text_input("Search")
    with c2: category = st.selectbox("Category", ["All"] + sorted(df.category.unique().tolist()))
    with c3: access = st.selectbox("Access", ["All"] + sorted(df.access.unique().tolist()))
    out = filter_tools(query, category, access)
    st.caption(f"{len(out)} matching tools · Last-reviewed fields are included in the dataset")
    st.dataframe(out[["tool","category","access","best_for","patient_data","citation_support","ease","last_verified"]], use_container_width=True, hide_index=True, height=560)
    st.download_button("Download directory CSV", df.to_csv(index=False).encode(), "careprompt_tool_directory.csv", "text/csv")
with tab2:
    task = st.text_area("Describe the task", placeholder="Example: find and organise evidence for a literature review")
    c1,c2 = st.columns(2)
    with c1:
        free = st.checkbox("Free access is mandatory", value=True)
        citations = st.checkbox("Citation traceability is essential", value=True)
    with c2:
        sensitive = st.checkbox("Sensitive data may be involved", value=False)
        technical = st.radio("User comfort", ["Beginner", "Advanced"], horizontal=True)
    if st.button("Recommend tools", type="primary"):
        if sensitive: st.warning("Use only institutionally approved systems. De-identification alone may not satisfy local policy.")
        rows = recommend(task, free, citations, sensitive, technical)
        if not rows: st.info("No exact match under the selected constraints. Relax one filter or use a locally approved tool.")
        for r in rows:
            with st.expander(f"{r['tool']} · {r['access']}", expanded=True):
                st.write(r['best_for']); st.caption("Limitation: " + r['limitations'])
                st.write("Patient data: **" + r['patient_data'] + "** | Citation support: **" + r['citation_support'] + "**")
                st.link_button("Official website", r['official_url'])
