import streamlit as st
import streamlit.components.v1 as components
from components.layout import page_header

page_header("Facilitator Mode", "Generate a workshop agenda, cases and debrief sequence for healthcare professionals.")
duration=st.selectbox("Programme duration", ["30 minutes","60 minutes","90 minutes","150 minutes","Half day","Full day"])
audience=st.multiselect("Audience", ["Doctors","Pharma professionals","Researchers","Healthcare managers"], default=["Doctors","Pharma professionals"])
focus=st.multiselect("Focus", ["Patient-centricity","Clinical reasoning","Research","Medical affairs","Pharmacovigilance","Professional projection","Responsible AI"], default=["Patient-centricity","Responsible AI"])
if st.button("Generate agenda", type="primary"):
    plans={
      "30 minutes":[("5 min","Safety and expectations"),("10 min","ChatGPT prompt demo"),("10 min","Participant challenge"),("5 min","Debrief")],
      "60 minutes":[("10 min","Foundations and safety"),("15 min","Patient-centric prompt demo"),("15 min","Research / pharma demo"),("15 min","Hands-on challenge"),("5 min","Debrief")],
      "90 minutes":[("15 min","Foundations"),("20 min","Three live demos"),("35 min","Guided lab"),("15 min","Case challenge"),("5 min","Commitment to action")],
      "150 minutes":[("20 min","GenAI and responsible use"),("25 min","Patient-centricity demos"),("15 min","Research and pharma tools"),("10 min","Break"),("55 min","Hands-on lab"),("15 min","Case competition"),("10 min","Debrief and action plan")],
      "Half day":[("45 min","Theory"),("60 min","Demonstrations"),("90 min","Hands-on lab"),("30 min","Case challenge"),("15 min","Debrief")],
      "Full day":[("90 min","Foundations and domain cases"),("90 min","Tool demonstrations"),("150 min","Hands-on labs"),("60 min","Team challenge"),("30 min","Presentations and debrief")],
    }
    st.table({"Time":[x[0] for x in plans[duration]],"Activity":[x[1] for x in plans[duration]]})
    st.info("Suggested facilitation rule: demonstrate with fictional data, reveal prompt improvements step-by-step, and require participants to identify one safety risk before accepting any output.")

st.subheader("Live session timer")
minutes=st.number_input("Minutes",1,180,15)
components.html(f"""<div style="font:700 42px system-ui;color:#0b6b66" id="timer">{int(minutes)}:00</div><button onclick="start()" style="padding:10px 18px">Start</button><script>function start(){{let s={int(minutes)*60};let e=document.getElementById('timer');let x=setInterval(()=>{{let m=Math.floor(s/60),r=s%60;e.innerText=m+':'+String(r).padStart(2,'0');s--;if(s<0)clearInterval(x)}},1000)}}</script>""", height=100)
