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


def test_build_schedule_includes_all_activities_when_they_fit():
    activities = [
        CareActivity("Feed", 10, 2),
        CareActivity("Walk", 15, 3),
        CareActivity("Play", 25, 1),
    ]
    planner = SchedulePlanner(activities, 60)

    schedule = planner.build_schedule()

    scheduled_names = [activity.activity_name for activity in schedule]
    assert sorted(scheduled_names) == ["Feed", "Play", "Walk"]
    assert planner.skipped_activities == []


def test_build_schedule_skips_activities_over_available_time_by_priority():
    high_priority = CareActivity("Medication", 40, 4)
    medium_priority = CareActivity("Walk", 30, 2)
    low_priority = CareActivity("Play", 25, 1)
    planner = SchedulePlanner([low_priority, medium_priority, high_priority], 60)

    schedule = planner.build_schedule()

    total_time = sum(activity.estimated_time for activity in schedule)
    assert total_time <= 60
    # Highest priority is scheduled first; the rest are skipped once time runs out.
    assert high_priority in schedule
    assert low_priority in planner.skipped_activities


def test_build_schedule_excludes_completed_activities():
    pending = CareActivity("Feed", 10, 2)
    done = CareActivity("Walk", 15, 3, True)
    planner = SchedulePlanner([pending, done], 60)

    schedule = planner.build_schedule()

    assert pending in schedule
    assert done not in schedule
    assert done in planner.skipped_activities


def test_weekly_recurring_activity_creates_next_occurrence_one_week_later():
    due_date = datetime(2026, 7, 7, 8, 0)
    activity = CareActivity("Feed", 10, 2, recurrence="weekly", due_date=due_date)

    next_activity = activity.complete_activity()

    assert activity.completed is True
    assert isinstance(next_activity, CareActivity)
    assert next_activity.completed is False
    assert next_activity.recurrence == "weekly"
    assert next_activity.due_date == due_date + timedelta(weeks=1)


def test_recurring_activity_without_due_date_returns_none():
    activity = CareActivity("Feed", 10, 2, recurrence="daily")

    next_activity = activity.complete_activity()

    assert activity.completed is True
    assert next_activity is None


def test_detect_conflicts_returns_no_warning_for_different_due_dates():
    first_activity = CareActivity("Feed", 10, 2, due_date=datetime(2026, 7, 7, 8, 0))
    second_activity = CareActivity("Walk", 15, 3, due_date=datetime(2026, 7, 7, 9, 0))
    planner = SchedulePlanner([first_activity, second_activity], 60)

    conflicts = planner.detect_conflicts()

    assert conflicts == []


def test_detect_conflicts_ignores_activities_without_due_dates():
    first_activity = CareActivity("Feed", 10, 2)
    second_activity = CareActivity("Walk", 15, 3, due_date=datetime(2026, 7, 7, 8, 0))
    planner = SchedulePlanner([first_activity, second_activity], 60)

    conflicts = planner.detect_conflicts()

    assert conflicts == []


def test_filter_by_completion_status_returns_only_completed_activities():
    activities = [
        CareActivity("Feed", 10, 2),
        CareActivity("Walk", 15, 3, True),
    ]
    planner = SchedulePlanner(activities, 60)

    completed_activities = planner.filter_by_completion_status(completed=True)

    assert [activity.activity_name for activity in completed_activities] == ["Walk"]
