from datetime import datetime, timedelta

from pawpal_system import CareActivity, PetProfile, SchedulePlanner


def test_complete_activity_marks_activity_as_completed():
    activity = CareActivity("Feed pet", 10, 2)

    activity.complete_activity()

    assert activity.completed is True


def test_adding_activity_increases_pet_activity_count():
    pet = PetProfile("Buddy", "Dog", 3, "Healthy")
    activity = CareActivity("Walk pet", 15, 1)

    pet.care_activities.append(activity)

    assert len(pet.care_activities) == 1


def test_sort_by_time_orders_activities_by_estimated_time():
    activities = [
        CareActivity("Play", 25, 1),
        CareActivity("Feed", 10, 2),
        CareActivity("Walk", 15, 3),
    ]
    planner = SchedulePlanner(activities, 60)

    sorted_activities = planner.sort_by_time()

    assert [activity.activity_name for activity in sorted_activities] == ["Feed", "Walk", "Play"]


def test_filter_by_completion_status_returns_only_matching_activities():
    activities = [
        CareActivity("Feed", 10, 2),
        CareActivity("Walk", 15, 3, True),
    ]
    planner = SchedulePlanner(activities, 60)

    pending_activities = planner.filter_by_completion_status(completed=False)

    assert [activity.activity_name for activity in pending_activities] == ["Feed"]


def test_recurring_activity_creates_next_occurrence_when_completed():
    due_date = datetime(2026, 7, 7, 8, 0)
    activity = CareActivity("Feed", 10, 2, recurrence="daily", due_date=due_date)

    next_activity = activity.complete_activity()

    assert activity.completed is True
    assert isinstance(next_activity, CareActivity)
    assert next_activity.completed is False
    assert next_activity.recurrence == "daily"
    assert next_activity.due_date == due_date + timedelta(days=1)


def test_detect_conflicts_returns_warning_for_same_due_date():
    first_activity = CareActivity("Feed", 10, 2, due_date=datetime(2026, 7, 7, 8, 0))
    second_activity = CareActivity("Walk", 15, 3, due_date=datetime(2026, 7, 7, 8, 0))
    planner = SchedulePlanner([first_activity, second_activity], 60)

    conflicts = planner.detect_conflicts()

    assert len(conflicts) == 1
    assert "same time" in conflicts[0].lower()
