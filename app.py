import streamlit as st
from planner import generate_plan

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
        st.session_state["plan"] = generate_plan(goal, days, hours, level)

if "plan" in st.session_state:
    st.subheader(f"Your roadmap: {st.session_state['goal']}")
    for item in st.session_state["plan"]:
        with st.expander(f"Day {item['day']} · {item['phase']}"):
            for task in item["tasks"]:
                st.write(f"- {task}")
            if item["mini_project"]:
                st.info(item["mini_project"])
            st.write("Resources:")
            for name, url in item["resources"].items():
                st.markdown(f"- [{name}]({url})")
