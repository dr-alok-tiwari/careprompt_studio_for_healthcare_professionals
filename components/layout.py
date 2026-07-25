from __future__ import annotations

import streamlit as st

from config.app_config import APP_NAME, APP_VERSION, COPYRIGHT
from config.theme import CSS


def apply_theme() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def _risk_class(risk: str) -> str:
    lowered = risk.lower()
    if "not suitable" in lowered or "high" in lowered:
        return "cp-badge-high"
    if "moderate" in lowered:
        return "cp-badge-moderate"
    return "cp-badge-low"


def page_header(title: str, subtitle: str, risk: str | None = None) -> None:
    risk_html = ""
    if risk:
        risk_html = f'<span class="cp-badge {_risk_class(risk)}">Risk level: {risk}</span>'
    st.markdown(
        f"""
        <div class="cp-hero">
          <div class="cp-hero-kicker">CarePrompt Studio · Responsible healthcare AI</div>
          <h1>{title}</h1>
          <p>{subtitle}</p>
          {risk_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar_brand() -> None:
    st.markdown(
        f"""
        <div class="cp-brand">
          <div class="cp-brand-kicker">Healthcare AI workbench</div>
          <div class="cp-brand-title">🩺 {APP_NAME}</div>
          <div class="cp-brand-copy">Guided prompts, tool choices and human-review safeguards.</div>
          <span class="cp-badge">Version {APP_VERSION}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_privacy_banner() -> None:
    st.markdown(
        """
        <div class="cp-warning">
          <b>🔒 Privacy first:</b> use fictional or de-identified information only. Never enter names,
          record numbers, contact details, exact addresses, identification numbers or identifiable images.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    st.markdown(
        f'<div class="cp-footer">{COPYRIGHT}<br>Not a medical device. High-risk outputs require qualified human review.</div>',
        unsafe_allow_html=True,
    )


def metric_card(title: str, value: str, caption: str) -> None:
    st.markdown(
        f"""
        <div class="cp-metric">
          <div class="cp-metric-label">{title}</div>
          <div class="cp-metric-value">{value}</div>
          <div class="cp-metric-copy">{caption}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def step_card(number: int, title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="cp-step">
          <div class="cp-step-number">{number}</div>
          <div><strong>{title}</strong><br><span>{body}</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def safe_callout(title: str, body: str) -> None:
    st.markdown(
        f'<div class="cp-safe"><b>{title}</b><br>{body}</div>',
        unsafe_allow_html=True,
    )
