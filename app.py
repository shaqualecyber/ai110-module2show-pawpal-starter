from datetime import datetime, date, time

import streamlit as st
from pawpal_system import PetProfile, CareActivity, OwnerProfile, SchedulePlanner

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
if "owner" not in st.session_state:
    st.session_state.owner = OwnerProfile(
        owner_name="Demo Owner",
        available_minutes=90,
        care_preferences="General pet care"
    )
st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

col4, col5 = st.columns(2)
with col4:
    due_time = st.time_input("Due time (used for conflict detection)", value=time(8, 0))
with col5:
    completed = st.checkbox("Already completed?")

if st.button("Add task"):
    st.session_state.tasks.append(
        {
            "title": task_title,
            "duration_minutes": int(duration),
            "priority": priority,
            "due_time": due_time.strftime("%H:%M"),
            "completed": completed,
        }
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

def activity_rows(activities):
    """Turn CareActivity objects into rows for a clean table display."""
    return [
        {
            "Task": activity.activity_name,
            "Minutes": activity.estimated_time,
            "Priority": activity.priority_level,
            "Due time": activity.due_date.strftime("%H:%M") if activity.due_date else "—",
            "Completed": "Yes" if activity.completed else "No",
        }
        for activity in activities
    ]


if st.button("Generate schedule"):
    priority_map = {"low": 1, "medium": 2, "high": 3}

    care_activities = [
        CareActivity(
            activity_name=task["title"],
            estimated_time=task["duration_minutes"],
            priority_level=priority_map[task["priority"]],
            completed=task.get("completed", False),
            due_date=datetime.combine(
                date.today(),
                datetime.strptime(task["due_time"], "%H:%M").time(),
            ) if task.get("due_time") else None,
        )
        for task in st.session_state.tasks
    ]

    planner = SchedulePlanner(
        activity_list=care_activities,
        available_minutes=st.session_state.owner.available_minutes
    )

    planner.build_schedule()

    # 1. Conflict detection — warn if two tasks share the same due time.
    conflicts = planner.detect_conflicts()
    if conflicts:
        for warning in conflicts:
            st.warning(warning)
    else:
        st.success("No scheduling conflicts found.")

    # 2. Today's schedule (what the planner chose to fit in the available time).
    st.subheader("Today's Schedule")
    if planner.daily_schedule:
        st.table(activity_rows(planner.daily_schedule))
    else:
        st.info("No activities were scheduled.")

    if planner.skipped_activities:
        st.caption(f"{len(planner.skipped_activities)} task(s) were skipped (out of time or already completed).")

    # 3. All tasks sorted by estimated time (shortest first).
    st.subheader("Sorted by Time")
    st.table(activity_rows(planner.sort_by_time()))

    # 4. Filter by completion status.
    st.subheader("Pending vs. Completed")
    pending = planner.filter_by_completion_status(completed=False)
    done = planner.filter_by_completion_status(completed=True)

    st.info(f"Pending tasks: {len(pending)} · Completed tasks: {len(done)}")

    col_pending, col_done = st.columns(2)
    with col_pending:
        st.markdown("**Pending**")
        if pending:
            st.table(activity_rows(pending))
        else:
            st.caption("No pending tasks.")
    with col_done:
        st.markdown("**Completed**")
        if done:
            st.table(activity_rows(done))
        else:
            st.caption("No completed tasks.")

    st.subheader("Why this schedule?")
    st.text(planner.explain_schedule())