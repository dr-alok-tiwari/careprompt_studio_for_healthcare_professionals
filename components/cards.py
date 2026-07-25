import streamlit as st


def action_card(title: str, description: str, badge: str = "") -> None:
    badge_html = f'<span class="cp-badge">{badge}</span>' if badge else ''
    st.markdown(f'<div class="cp-card"><h3>{title}</h3><p>{description}</p>{badge_html}</div>', unsafe_allow_html=True)


def review_checklist(items: list[str], key_prefix: str) -> None:
    st.markdown("#### Human-review checklist")
    for i, item in enumerate(items):
        st.checkbox(item, key=f"{key_prefix}_{i}")
