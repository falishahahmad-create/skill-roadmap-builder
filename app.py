import streamlit as st

st.set_page_config(page_title="Skill Roadmap Builder", page_icon="🗺️", layout="wide")

st.title("🗺️ Skill Roadmap Builder")
st.write("Tell me what you want to learn and I'll build a day-by-day plan.")

with st.form("goal_form"):
    goal = st.text_input("What's your goal?", placeholder="e.g. Become a data analyst")
    days = st.slider("How many days do you have?", 7, 90, 30)
    hours = st.slider("Hours you can study per day", 1, 8, 2)
    level = st.selectbox("Your current level", ["Beginner", "Some experience", "Intermediate"])
    submitted = st.form_submit_button("Create my roadmap")

if submitted:
    if not goal.strip():
        st.warning("Please enter a goal first.")
    else:
        st.session_state["goal"] = goal
        st.session_state["days"] = days
        st.session_state["hours"] = hours
        st.session_state["level"] = level
        st.success(f"Goal saved: {goal} in {days} days, {hours} hrs/day ({level})")
