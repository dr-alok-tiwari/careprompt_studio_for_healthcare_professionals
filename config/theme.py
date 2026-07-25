CSS = r"""
<style>
:root {
  --brand: #0b6b66;
  --brand-dark: #064a47;
  --accent: #d97706;
  --soft: #eef8f7;
  --text: #16302f;
}
html, body, [class*="css"] { font-size: 17px; }
.block-container { max-width: 1280px; padding-top: 1.3rem; padding-bottom: 2rem; }
h1 { color: var(--brand-dark); letter-spacing: -0.02em; }
h2, h3 { color: var(--brand); }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #f4fbfa 0%, #ffffff 100%); }
.cp-hero { padding: 1.5rem 1.6rem; border-radius: 20px; background: linear-gradient(135deg,#e7f7f5,#fff8ec); border: 1px solid #cfe8e5; margin-bottom: 1rem; }
.cp-card { padding: 1rem 1.1rem; border-radius: 16px; border: 1px solid #dce8e6; background: white; min-height: 150px; box-shadow: 0 4px 14px rgba(10,70,66,.05); }
.cp-badge { display:inline-block; padding:.22rem .58rem; margin:.1rem .18rem .1rem 0; border-radius:999px; background:#e8f4f3; color:#075d58; font-size:.82rem; font-weight:600; }
.cp-warning { padding:.8rem 1rem; border-left:5px solid #d97706; background:#fff8ed; border-radius:8px; }
.cp-safe { padding:.8rem 1rem; border-left:5px solid #0b6b66; background:#edf9f7; border-radius:8px; }
.cp-footer { text-align:center; color:#667; font-size:.82rem; padding:2rem .5rem .4rem; }
.stButton > button, .stDownloadButton > button { min-height: 44px; border-radius: 10px; font-weight: 600; }
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] { font-size: 1rem; }
.copy-box { display:flex; gap:.6rem; align-items:center; }
@media (max-width: 700px) { html, body, [class*="css"] { font-size: 16px; } }
</style>
"""
