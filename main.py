from pawpal_system import PetProfile, CareActivity, OwnerProfile, SchedulePlanner


# Create the owner
owner = OwnerProfile(
    owner_name="Alex",
    available_minutes=90,
    care_preferences="Morning routine and medication"
)

# Create pets
milo = PetProfile(
    pet_name="Milo",
    species="Dog",
    age=4,
    health_notes="Needs regular walks"
)

luna = PetProfile(
    pet_name="Luna",
    species="Cat",
    age=2,
    health_notes="Prefers quiet playtime"
)

# Create care activities out of order
walk = CareActivity("Morning walk", 20, 3)
feed = CareActivity("Feed breakfast", 10, 2)
medication = CareActivity("Give medication", 15, 4)
play = CareActivity("Play session", 25, 1)

# Mark one task as completed to demonstrate filtering
play.complete_activity()

# Assign activities to pets
milo.care_activities.extend([walk, feed])
luna.care_activities.extend([medication, play])

# Add pets to the owner
owner.add_pet(milo)
owner.add_pet(luna)

# Gather all care activities from the owner
all_activities = owner.get_all_care_activities()

# Create a planner using the owner's available time
planner = SchedulePlanner(all_activities, owner.available_minutes)
planner.build_schedule()

# Demonstrate sorting by time
sorted_activities = planner.sort_by_time()

# Demonstrate filtering by completion status
pending_activities = planner.filter_by_completion_status(completed=False)

# Print the schedule
print("Today's Schedule")
print("=" * 20)
for activity in planner.daily_schedule:
    print(f"- {activity.activity_name} ({activity.estimated_time} min, priority {activity.priority_level})")

print("\nSorted by time:")
for activity in sorted_activities:
    print(f"- {activity.activity_name} ({activity.estimated_time} min)")

print("\nPending tasks:")
for activity in pending_activities:
    print(f"- {activity.activity_name} ({activity.estimated_time} min)")

print("\n" + planner.explain_schedule())
