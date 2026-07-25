import streamlit as st
import streamlit.components.v1 as components

from components.guided_inputs import guided_text_area
from components.layout import page_header, safe_callout

page_header(
    "Facilitator Mode",
    "Generate a workshop agenda, guided demonstrations and debrief sequence for healthcare professionals.",
)

safe_callout(
    "Workshop-ready design",
    "Select a structure, start from a sample learning goal or type your own, and generate an agenda that keeps privacy and human oversight visible.",
)

c1, c2 = st.columns(2)
with c1:
    duration = st.selectbox(
        "Programme duration",
        ["30 minutes", "60 minutes", "90 minutes", "150 minutes", "Half day", "Full day"],
        key="facilitator_duration",
    )
    audience = st.multiselect(
        "Audience",
        ["Doctors", "Pharma professionals", "Researchers", "Healthcare managers"],
        default=["Doctors", "Pharma professionals"],
        key="facilitator_audience",
    )
with c2:
    focus = st.multiselect(
        "Focus",
        [
            "Patient-centricity",
            "Clinical reasoning",
            "Research",
            "Medical affairs",
            "Pharmacovigilance",
            "Professional projection",
            "Responsible AI",
        ],
        default=["Patient-centricity", "Responsible AI"],
        key="facilitator_focus",
    )
    experience = st.radio(
        "Participant AI experience",
        ["Mostly beginners", "Mixed group", "Mostly experienced"],
        horizontal=True,
        key="facilitator_experience",
    )

learning_goal = guided_text_area(
    "Workshop learning goal",
    key="facilitator_goal",
    samples=[
        "By the end of the session, participants will build and critique one patient-centred ChatGPT prompt, identify three safety risks, and select an appropriate alternative AI tool.",
        "Participants will compare weak and expert prompts for research, medical affairs and clinical education, then produce a reviewed prompt for their own non-sensitive task.",
        "Participants will complete a fictional case challenge, verify evidence requirements, and create a practical 30-day responsible-AI action plan.",
    ],
    placeholder="Type a measurable learning outcome in your own words.",
    height=135,
)

custom_activity = st.text_input(
    "Optional custom activity",
    key="facilitator_custom_activity",
    placeholder="Example: 15-minute team prompt competition with peer scoring",
)

plans = {
    "30 minutes": [
        ("5 min", "Safety, privacy and expectations"),
        ("8 min", "One guided ChatGPT prompt demonstration"),
        ("10 min", "Participant prompt challenge"),
        ("5 min", "Peer review using CRAFT-MED"),
        ("2 min", "Commitment to action"),
    ],
    "60 minutes": [
        ("10 min", "Foundations, limitations and safe-use rules"),
        ("15 min", "Patient-centric prompt demonstration"),
        ("12 min", "Research or pharma tool demonstration"),
        ("18 min", "Hands-on guided challenge"),
        ("5 min", "Debrief and action plan"),
    ],
    "90 minutes": [
        ("15 min", "Foundations and responsible use"),
        ("20 min", "Three short domain demonstrations"),
        ("30 min", "Guided individual lab"),
        ("20 min", "Team case challenge and critique"),
        ("5 min", "Commitment to action"),
    ],
    "150 minutes": [
        ("20 min", "Generative AI, limitations and privacy"),
        ("25 min", "Patient-centricity demonstrations"),
        ("15 min", "Research and pharma tools"),
        ("10 min", "Break"),
        ("50 min", "Hands-on guided lab"),
        ("20 min", "Case competition and peer review"),
        ("10 min", "Debrief and action plan"),
    ],
    "Half day": [
        ("45 min", "Theory and responsible-use framework"),
        ("60 min", "Domain demonstrations"),
        ("90 min", "Hands-on guided labs"),
        ("30 min", "Case challenge"),
        ("15 min", "Debrief and transfer plan"),
    ],
    "Full day": [
        ("90 min", "Foundations, safety and domain cases"),
        ("90 min", "Tool demonstrations"),
        ("150 min", "Hands-on labs"),
        ("60 min", "Team challenge"),
        ("30 min", "Presentations, feedback and action plan"),
    ],
}

if st.button("Generate workshop agenda", type="primary", use_container_width=True):
    selected_plan = list(plans[duration])
    if custom_activity.strip():
        selected_plan.insert(-1, ("Flexible", custom_activity.strip()))

    st.markdown("#### Workshop brief")
    st.write(f"**Audience:** {', '.join(audience) if audience else 'Healthcare professionals'}")
    st.write(f"**Focus:** {', '.join(focus) if focus else 'Responsible healthcare AI'}")
    st.write(f"**Experience:** {experience}")
    st.write(f"**Learning goal:** {learning_goal or 'Build and review a responsible healthcare prompt.'}")

    st.markdown("#### Suggested agenda")
    st.table({"Time": [item[0] for item in selected_plan], "Activity": [item[1] for item in selected_plan]})

    st.markdown("#### Facilitation nudges")
    nudges = [
        "Demonstrate only with fictional or de-identified information.",
        "Reveal prompt improvements step-by-step rather than showing only the final prompt.",
        "Ask participants to identify one privacy risk and one factuality risk before accepting an output.",
        "Prioritise free tools, then explain when a specialised paid tool is justified.",
        "Require a named human reviewer for every high-risk workflow.",
        "End with one task participants will apply within 30 days.",
    ]
    for item in nudges:
        st.write("- " + item)

st.subheader("Live session timer")
minutes = st.number_input(
    "Minutes",
    min_value=1,
    max_value=180,
    value=15,
    step=1,
    key="facilitator_timer_minutes",
)
components.html(
    f"""
    <div style="font:800 44px system-ui;color:#0F766E;margin-bottom:8px" id="timer">{int(minutes)}:00</div>
    <button onclick="startTimer()" style="padding:11px 20px;border-radius:10px;border:0;background:#0B1F33;color:white;font-weight:700;cursor:pointer">Start timer</button>
    <button onclick="resetTimer()" style="padding:11px 20px;border-radius:10px;border:1px solid #AFC8CD;background:white;color:#0B1F33;font-weight:700;cursor:pointer">Reset</button>
    <script>
      let initial = {int(minutes) * 60};
      let remaining = initial;
      let interval = null;
      const timer = document.getElementById('timer');
      function paint() {{
        const m = Math.floor(remaining / 60);
        const s = remaining % 60;
        timer.innerText = m + ':' + String(s).padStart(2, '0');
      }}
      function startTimer() {{
        if (interval) return;
        interval = setInterval(() => {{
          remaining -= 1;
          paint();
          if (remaining <= 0) {{ clearInterval(interval); interval = null; }}
        }}, 1000);
      }}
      function resetTimer() {{
        if (interval) clearInterval(interval);
        interval = null;
        remaining = initial;
        paint();
      }}
    </script>
    """,
    height=120,
)
