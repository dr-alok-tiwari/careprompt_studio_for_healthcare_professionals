CSS = r"""
<style>
:root {
  --cp-navy: #0B1F33;
  --cp-teal: #0F766E;
  --cp-mint: #14B8A6;
  --cp-sky: #EAF7F6;
  --cp-ice: #F5FAFC;
  --cp-amber: #F59E0B;
  --cp-coral: #E76F51;
  --cp-text: #152536;
  --cp-muted: #5C6B78;
  --cp-border: #D7E5E8;
  --cp-surface: #FFFFFF;
  --cp-shadow: 0 12px 34px rgba(11, 31, 51, 0.08);
}

html, body, [class*="css"] {
  font-size: 17px;
  color: var(--cp-text);
}

.stApp {
  background:
    radial-gradient(circle at 8% 4%, rgba(20,184,166,.08), transparent 24rem),
    radial-gradient(circle at 92% 12%, rgba(245,158,11,.07), transparent 22rem),
    linear-gradient(180deg, #FBFDFE 0%, #F5FAFC 100%);
}

.block-container {
  max-width: 1320px;
  padding-top: 1.15rem;
  padding-bottom: 2.5rem;
}

h1, h2, h3 {
  letter-spacing: -0.025em;
}

h1 { color: var(--cp-navy); font-weight: 800; }
h2 { color: var(--cp-navy); font-weight: 750; }
h3 { color: var(--cp-teal); font-weight: 700; }
p, li { line-height: 1.62; }

[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #071B2B 0%, #0B2E3D 55%, #0F5D5A 100%);
  border-right: 0;
}
[data-testid="stSidebar"] * { color: #F3FBFC; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] .stCaption { color: #C8E5E5 !important; }
[data-testid="stSidebar"] [data-baseweb="radio"] label,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] { color: #F7FFFF !important; }
[data-testid="stSidebarNav"] a { border-radius: 11px; margin: 2px 8px; }
[data-testid="stSidebarNav"] a:hover { background: rgba(255,255,255,.10); }

.cp-brand {
  padding: 1rem 1rem .9rem;
  border: 1px solid rgba(255,255,255,.16);
  background: rgba(255,255,255,.08);
  border-radius: 18px;
  margin-bottom: .8rem;
}
.cp-brand-kicker {
  color: #9CE4DB;
  font-size: .74rem;
  font-weight: 800;
  letter-spacing: .11em;
  text-transform: uppercase;
}
.cp-brand-title { color: white; font-size: 1.42rem; font-weight: 850; margin: .2rem 0; }
.cp-brand-copy { color: #CBE6E6; font-size: .88rem; line-height: 1.45; }

.cp-hero {
  position: relative;
  overflow: hidden;
  padding: 1.7rem 1.85rem;
  border-radius: 24px;
  background: linear-gradient(125deg, #0B1F33 0%, #0E5361 52%, #0F766E 100%);
  border: 1px solid rgba(255,255,255,.18);
  box-shadow: var(--cp-shadow);
  margin-bottom: 1.2rem;
}
.cp-hero::after {
  content: "";
  position: absolute;
  width: 240px;
  height: 240px;
  border-radius: 50%;
  right: -80px;
  top: -110px;
  background: rgba(255,255,255,.09);
}
.cp-hero-kicker {
  color: #A9EFE5;
  font-size: .77rem;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  margin-bottom: .35rem;
}
.cp-hero h1 { color: #FFFFFF; margin: 0 0 .38rem; font-size: clamp(2rem, 4vw, 3rem); }
.cp-hero p { color: #DCEFF1; margin: 0; max-width: 900px; font-size: 1.04rem; }
.cp-hero .cp-badge { margin-top: .75rem; }

.cp-card {
  height: 100%;
  padding: 1.05rem 1.15rem;
  border-radius: 18px;
  border: 1px solid var(--cp-border);
  background: rgba(255,255,255,.94);
  box-shadow: 0 7px 22px rgba(11,31,51,.055);
  transition: transform .16s ease, box-shadow .16s ease, border-color .16s ease;
}
.cp-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 13px 30px rgba(11,31,51,.09);
  border-color: #A9D7D5;
}
.cp-card h3 { margin-top: 0; }
.cp-card p { color: var(--cp-muted); }

.cp-metric {
  min-height: 135px;
  padding: 1.05rem 1.1rem;
  border-radius: 18px;
  background: linear-gradient(145deg, #FFFFFF 0%, #F4FBFB 100%);
  border: 1px solid var(--cp-border);
  box-shadow: 0 7px 22px rgba(11,31,51,.05);
}
.cp-metric-label { color: var(--cp-muted); font-size: .82rem; font-weight: 750; text-transform: uppercase; letter-spacing: .06em; }
.cp-metric-value { color: var(--cp-navy); font-size: 2rem; font-weight: 850; margin: .15rem 0; }
.cp-metric-copy { color: var(--cp-muted); font-size: .88rem; }

.cp-badge {
  display: inline-block;
  padding: .28rem .65rem;
  margin: .1rem .25rem .1rem 0;
  border-radius: 999px;
  background: #DDF6F2;
  color: #075D58;
  border: 1px solid #B9E8E1;
  font-size: .8rem;
  font-weight: 750;
}
.cp-badge-high { background:#FFF0E8; color:#9B351E; border-color:#F5C6B7; }
.cp-badge-moderate { background:#FFF7DD; color:#855B00; border-color:#F3D88C; }
.cp-badge-low { background:#E4F8EF; color:#12633E; border-color:#BCE8D1; }

.cp-warning, .cp-safe, .cp-info {
  padding: .88rem 1rem;
  border-radius: 13px;
  margin: .35rem 0 .8rem;
  border: 1px solid;
}
.cp-warning { border-color: #F0C59D; border-left: 5px solid var(--cp-amber); background: #FFF8ED; color:#6F4510; }
.cp-safe { border-color:#B7E2DB; border-left:5px solid var(--cp-teal); background:#EFFAF8; color:#154D49; }
.cp-info { border-color:#BDDCE8; border-left:5px solid #2683A2; background:#F0F8FB; color:#1B5367; }

.cp-step {
  display:flex;
  gap:.8rem;
  align-items:flex-start;
  padding:.9rem 1rem;
  border-radius:15px;
  background:#FFFFFF;
  border:1px solid var(--cp-border);
  margin-bottom:.65rem;
}
.cp-step-number {
  flex:0 0 34px;
  width:34px;
  height:34px;
  border-radius:50%;
  display:grid;
  place-items:center;
  color:white;
  background:linear-gradient(135deg,var(--cp-teal),var(--cp-mint));
  font-weight:800;
}
.cp-step strong { color:var(--cp-navy); }

[data-testid="stForm"], [data-testid="stExpander"] {
  border-color: var(--cp-border) !important;
  border-radius: 16px !important;
  background: rgba(255,255,255,.86);
}

[data-baseweb="tab-list"] { gap: .45rem; }
[data-baseweb="tab"] {
  border-radius: 999px;
  padding: .48rem .85rem;
  background: #EDF5F6;
  color: var(--cp-navy);
}
[aria-selected="true"][data-baseweb="tab"] {
  background: var(--cp-navy);
  color: white;
}

.stButton > button, .stDownloadButton > button, [data-testid="stLinkButton"] a {
  min-height: 46px;
  border-radius: 12px;
  font-weight: 750;
  border-color: #B9D4D8;
}
.stButton > button[kind="primary"] {
  background: linear-gradient(135deg, #0F766E 0%, #0B5966 100%);
  border: 0;
  box-shadow: 0 7px 16px rgba(15,118,110,.22);
}
.stButton > button:hover, .stDownloadButton > button:hover {
  border-color: var(--cp-teal);
  transform: translateY(-1px);
}

[data-testid="stWidgetLabel"] p { font-weight: 720; color: var(--cp-navy); }
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"], .stMultiSelect div[data-baseweb="select"] {
  font-size: 1rem;
}
.stTextInput input, .stTextArea textarea {
  border-radius: 12px;
}
.stTextArea textarea:focus, .stTextInput input:focus {
  border-color: var(--cp-teal) !important;
  box-shadow: 0 0 0 2px rgba(20,184,166,.12) !important;
}

[data-testid="stDataFrame"], [data-testid="stTable"] {
  border: 1px solid var(--cp-border);
  border-radius: 14px;
  overflow: hidden;
}

.cp-footer {
  text-align:center;
  color:#667887;
  font-size:.82rem;
  padding:2.3rem .5rem .5rem;
}

@media (max-width: 760px) {
  html, body, [class*="css"] { font-size: 16px; }
  .block-container { padding-top: .75rem; }
  .cp-hero { padding: 1.35rem 1.2rem; border-radius: 18px; }
  .cp-hero h1 { font-size: 2rem; }
  .cp-card, .cp-metric { min-height: auto; }
}
</style>
"""
