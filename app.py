import streamlit as st

# App title
st.title("ADHD Coach")

# Introduction
st.markdown("""
Welcome to your personal ADHD coach! This app is here to help you manage overwhelm, prioritize tasks, 
and provide support when you're feeling stuck or stressed.
""")

# Sidebar for navigation
st.sidebar.header("Navigation")
options = st.sidebar.radio("Choose a function:", [
    "Prioritize Tasks",
    "Daily Planner",
    "Overwhelm Support",
    "ADHD Insights",
])

# Prioritize Tasks
if options == "Prioritize Tasks":
    st.header("Task Prioritizer")
    st.markdown("Input your tasks below, and we'll help you rank them by importance and urgency.")

    tasks = st.text_area("Enter your tasks (one per line):")
    if st.button("Prioritize"):
        if tasks.strip():
            task_list = tasks.split("\n")
            st.markdown("Here are your tasks, ranked by priority:")
            for idx, task in enumerate(task_list, start=1):
                st.write(f"{idx}. {task}")
        else:
            st.warning("Please enter some tasks.")

# Daily Planner
if options == "Daily Planner":
    st.header("Daily Planner")
    st.markdown("Plan your day and block time for key activities.")

    wake_time = st.time_input("What time will you wake up?")
    sleep_time = st.time_input("What time will you go to bed?")
    key_tasks = st.text_area("Key tasks for the day (one per line):")
    if st.button("Create Plan"):
        st.markdown(f"**Wake up at:** {wake_time}")
        st.markdown(f"**Go to bed at:** {sleep_time}")
        if key_tasks.strip():
            st.markdown("### Key tasks:")
            for task in key_tasks.split("\n"):
                st.write(f"- {task}")
        else:
            st.warning("Please enter some key tasks.")

# Overwhelm Support
if options == "Overwhelm Support":
    st.header("Overwhelm Support")
    st.markdown("Feeling overwhelmed? Use this tool to ground yourself.")

    st.markdown("Take a deep breath and try this grounding exercise:")
    st.write("1. Name 5 things you can see.")
    st.write("2. Name 4 things you can touch.")
    st.write("3. Name 3 things you can hear.")
    st.write("4. Name 2 things you can smell.")
    st.write("5. Name 1 thing you can taste.")

# ADHD Insights
if options == "ADHD Insights":
    st.header("ADHD Insights")
    st.markdown("Get tips and strategies for managing ADHD.")
    tips = [
        "Break tasks into smaller steps.",
        "Use timers to stay focused.",
        "Create a visual task board.",
        "Reward yourself for completing tasks.",
        "Establish routines for repetitive activities.",
    ]
    st.markdown("Here are some tips for today:")
    for tip in tips:
        st.write(f"- {tip}")

# Footer
st.markdown("### Powered by Streamlit")
