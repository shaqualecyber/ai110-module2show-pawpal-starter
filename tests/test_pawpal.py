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
