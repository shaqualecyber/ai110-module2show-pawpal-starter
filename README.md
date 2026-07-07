# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

## Sample Output

```text
Today's Schedule
====================

- Give medication (15 min, priority 4)
- Morning walk (20 min, priority 3)
- Feed breakfast (10 min, priority 2)
- Play session (25 min, priority 1)

Daily Schedule Explanation
Available Time: 90 minutes
========================================

INCLUDED ACTIVITIES (4 tasks):
1. Give medication
   Time: 15 min | Priority: 4
2. Morning walk
   Time: 20 min | Priority: 3
3. Feed breakfast
   Time: 10 min | Priority: 2
4. Play session
   Time: 25 min | Priority: 1

Total Time Used: 70 minutes
Time Remaining: 20 minutes

SKIPPED ACTIVITIES (0 tasks):
```

## 🧪 Testing PawPal+

Run the full automated test suite from the project root with:

```bash
python3 -m pytest
```

### What the tests verify

The automated tests check the core logic that PawPal+ relies on to build a trustworthy daily plan:

- **Sorting behavior** — activities can be ordered from the shortest estimated time to the longest.
- **Filtering behavior** — the planner can return just the completed tasks or just the pending ones.
- **Recurring task logic** — completing a daily or weekly task correctly creates the next occurrence on the right date, and a recurring task with no due date does not create one.
- **Conflict detection** — the planner warns when two tasks are scheduled for the same time, and stays quiet when times differ or are missing.
- **Schedule building** — the planner packs the highest-priority tasks into the available time, skips tasks that do not fit, and leaves out tasks that are already completed.

### Successful test run

```text
============================= test session starts ==============================
platform darwin -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0 -- /usr/local/bin/python3
cachedir: .pytest_cache
rootdir: /Users/quale/Desktop/ai110-module2show-pawpal-starter
plugins: anyio-4.14.0
collecting ... collected 14 items

tests/test_pawpal.py::test_complete_activity_marks_activity_as_completed PASSED [  7%]
tests/test_pawpal.py::test_adding_activity_increases_pet_activity_count PASSED [ 14%]
tests/test_pawpal.py::test_sort_by_time_orders_activities_by_estimated_time PASSED [ 21%]
tests/test_pawpal.py::test_filter_by_completion_status_returns_only_matching_activities PASSED [ 28%]
tests/test_pawpal.py::test_recurring_activity_creates_next_occurrence_when_completed PASSED [ 35%]
tests/test_pawpal.py::test_detect_conflicts_returns_warning_for_same_due_date PASSED [ 42%]
tests/test_pawpal.py::test_build_schedule_includes_all_activities_when_they_fit PASSED [ 50%]
tests/test_pawpal.py::test_build_schedule_skips_activities_over_available_time_by_priority PASSED [ 57%]
tests/test_pawpal.py::test_build_schedule_excludes_completed_activities PASSED [ 64%]
tests/test_pawpal.py::test_weekly_recurring_activity_creates_next_occurrence_one_week_later PASSED [ 71%]
tests/test_pawpal.py::test_recurring_activity_without_due_date_returns_none PASSED [ 78%]
tests/test_pawpal.py::test_detect_conflicts_returns_no_warning_for_different_due_dates PASSED [ 85%]
tests/test_pawpal.py::test_detect_conflicts_ignores_activities_without_due_dates PASSED [ 92%]
tests/test_pawpal.py::test_filter_by_completion_status_returns_only_completed_activities PASSED [100%]

============================== 14 passed in 0.10s ==============================
```

### Confidence level

**★★★★★ (5 / 5)**

All 14 automated tests passed successfully, and the implemented scheduling features behaved exactly as expected. The suite covers every core behavior — sorting, filtering, recurring task logic, conflict detection, and schedule building — including important edge cases like over-budget schedules and recurring tasks with no due date, giving full confidence in the scheduling logic.

## 📐 Smarter Scheduling


| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Sorting behavior | `SchedulePlanner.sort_by_time()` | Orders care activities by their estimated time from shortest to longest. |
| Filtering behavior | `SchedulePlanner.filter_by_completion_status()` | Returns only completed or pending activities based on the chosen status. |
| Conflict detection logic | `SchedulePlanner.detect_conflicts()` | Warns when two activities share the same due date and time. |
| Recurring task logic | `CareActivity.complete_activity()` | Marks an activity complete and creates the next daily or weekly occurrence when applicable. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
