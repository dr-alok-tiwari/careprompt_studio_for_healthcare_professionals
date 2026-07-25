import streamlit as st
from pathlib import Path
from components.layout import page_header
from utils.helpers import load_json

page_header("Resource Library", "Downloadable checklists, prompt guides and workshop-ready synthetic datasets.")
resources=load_json("resource_links.json")
for r in resources:
    with st.expander(r['title']):
        st.write(r['description']); st.caption("Last reviewed: "+r['last_reviewed'])
        if r.get('url'): st.link_button("Open official resource", r['url'])

st.subheader("Synthetic workshop datasets")
data_dir=Path(__file__).resolve().parents[1]/"data"/"synthetic"
for path in sorted(data_dir.glob("*.csv")):
    c1,c2=st.columns([3,1])
    c1.write(path.stem.replace("_"," ").title())
    c2.download_button("Download", path.read_bytes(), path.name, "text/csv", key=path.name)
