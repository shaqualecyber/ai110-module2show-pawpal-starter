from pawpal_system import CareActivity, PetProfile


def test_complete_activity_marks_activity_as_completed():
    activity = CareActivity("Feed pet", 10, 2)

    activity.complete_activity()

    assert activity.completed is True


def test_adding_activity_increases_pet_activity_count():
    pet = PetProfile("Buddy", "Dog", 3, "Healthy")
    activity = CareActivity("Walk pet", 15, 1)

    pet.care_activities.append(activity)

    assert len(pet.care_activities) == 1
