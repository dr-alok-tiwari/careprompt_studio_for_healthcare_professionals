import streamlit as st
from config.theme import CSS
from config.app_config import COPYRIGHT


def apply_theme() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def page_header(title: str, subtitle: str, risk: str | None = None) -> None:
    risk_html = f'<span class="cp-badge">Risk: {risk}</span>' if risk else ''
    st.markdown(
        f'<div class="cp-hero"><h1>{title}</h1><p>{subtitle}</p>{risk_html}</div>',
        unsafe_allow_html=True,
    )


def render_privacy_banner() -> None:
    with st.container():
        st.markdown(
            '<div class="cp-warning"><b>Privacy reminder:</b> use fictional or de-identified information only. Do not enter names, record numbers, exact addresses, phone numbers, identification numbers, or identifiable images.</div>',
            unsafe_allow_html=True,
        )


def render_footer() -> None:
    st.markdown(f'<div class="cp-footer">{COPYRIGHT}<br>Not a medical device. Outputs require qualified human review.</div>', unsafe_allow_html=True)


def metric_card(title: str, value: str, caption: str) -> None:
    st.markdown(f'<div class="cp-card"><h3>{title}</h3><h2>{value}</h2><p>{caption}</p></div>', unsafe_allow_html=True)
