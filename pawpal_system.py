from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class PetProfile:
    """Represents a pet's profile with basic information."""
    pet_name: str
    species: str
    age: int
    health_notes: str
    care_activities: list = field(default_factory=list)

    def update_pet_info(self, pet_name=None, species=None, age=None, health_notes=None):
        """Update the pet's information."""
        if pet_name is not None:
            self.pet_name = pet_name
        if species is not None:
            self.species = species
        if age is not None:
            self.age = age
        if health_notes is not None:
            self.health_notes = health_notes

    def view_pet_details(self):
        """View the pet's details."""
        details = f"Pet: {self.pet_name}\n"
        details += f"Species: {self.species}\n"
        details += f"Age: {self.age} years\n"
        details += f"Health Notes: {self.health_notes}\n"
        details += f"Care Activities: {len(self.care_activities)} total"
        return details


class OwnerProfile:
    """Represents a pet owner's profile and preferences."""
    
    def __init__(self, owner_name: str, available_minutes: int, care_preferences: str):
        self.owner_name = owner_name
        self.available_minutes = available_minutes
        self.care_preferences = care_preferences
        self.pet_profiles = []

    def add_pet(self, pet_profile: PetProfile):
        """Add a pet profile to the owner's list."""
        self.pet_profiles.append(pet_profile)

    def update_availability(self, available_minutes=None):
        """Update the owner's available time."""
        if available_minutes is not None:
            self.available_minutes = available_minutes

    def update_preferences(self, care_preferences=None):
        """Update the owner's care preferences."""
        if care_preferences is not None:
            self.care_preferences = care_preferences

    def get_all_care_activities(self):
        """Get all care activities from all pets."""
        all_activities = []
        for pet in self.pet_profiles:
            all_activities.extend(pet.care_activities)
        return all_activities


@dataclass
class CareActivity:
    """Represents a care activity for the pet."""
    activity_name: str
    estimated_time: int
    priority_level: int
    completed: bool = False
    recurrence: str = "none"
    due_date: datetime | None = None

    def edit_activity(self, activity_name=None, estimated_time=None, priority_level=None):
        """Edit the activity details."""
        if activity_name is not None:
            self.activity_name = activity_name
        if estimated_time is not None:
            self.estimated_time = estimated_time
        if priority_level is not None:
            self.priority_level = priority_level

    def complete_activity(self):
        """Mark the activity as completed and create the next repeat if it is recurring."""
        self.completed = True

        if self.recurrence == "daily" and self.due_date is not None:
            return CareActivity(
                activity_name=self.activity_name,
                estimated_time=self.estimated_time,
                priority_level=self.priority_level,
                completed=False,
                recurrence=self.recurrence,
                due_date=self.due_date + timedelta(days=1),
            )

        if self.recurrence == "weekly" and self.due_date is not None:
            return CareActivity(
                activity_name=self.activity_name,
                estimated_time=self.estimated_time,
                priority_level=self.priority_level,
                completed=False,
                recurrence=self.recurrence,
                due_date=self.due_date + timedelta(weeks=1),
            )

        return None


class SchedulePlanner:
    """Manages and plans the pet's daily care schedule."""
    
    def __init__(self, activity_list: list, available_minutes: int):
        self.activity_list = activity_list
        self.available_minutes = available_minutes
        self.daily_schedule = []
        self.skipped_activities = []

    def sort_by_time(self):
        """Return activities ordered from shortest to longest estimated time."""
        return sorted(self.activity_list, key=lambda activity: activity.estimated_time)

    def filter_by_completion_status(self, completed=False):
        """Return only the activities that match the chosen completed or pending status."""
        return [activity for activity in self.activity_list if activity.completed is completed]

    def detect_conflicts(self):
        """Return warning messages when two activities share the same due date and time."""
        warnings = []
        for index, activity in enumerate(self.activity_list):
            for other_activity in self.activity_list[index + 1:]:
                if activity.due_date is not None and other_activity.due_date is not None:
                    if activity.due_date == other_activity.due_date:
                        warnings.append(
                            f"Conflict: {activity.activity_name} and {other_activity.activity_name} are scheduled for the same time ({activity.due_date})."
                        )
        return warnings

    def prioritize_tasks(self):
        """Prioritize tasks based on importance and time."""
        # Sort activities by priority level (highest first), then by estimated time (shortest first)
        return sorted(self.activity_list, key=lambda x: (-x.priority_level, x.estimated_time))

    def build_schedule(self):
        """Build a daily schedule from available activities."""
        # Reset schedule and skipped activities
        self.daily_schedule = []
        self.skipped_activities = []
        
        # Get prioritized list of activities
        prioritized = self.prioritize_tasks()
        
        total_time_used = 0
        
        # Try to fit each activity into the schedule
        for activity in prioritized:
            if not activity.completed:
                # Check if activity fits within available time
                if total_time_used + activity.estimated_time <= self.available_minutes:
                    self.daily_schedule.append(activity)
                    total_time_used += activity.estimated_time
                else:
                    self.skipped_activities.append(activity)
            else:
                # Skip already completed activities
                self.skipped_activities.append(activity)
        
        return self.daily_schedule

    def explain_schedule(self):
        """Explain the reasoning behind the schedule."""
        explanation = f"Daily Schedule Explanation\n"
        explanation += f"Available Time: {self.available_minutes} minutes\n"
        explanation += f"─" * 40 + "\n\n"
        
        explanation += f"INCLUDED ACTIVITIES ({len(self.daily_schedule)} tasks):\n"
        total_time = 0
        for i, activity in enumerate(self.daily_schedule, 1):
            explanation += f"{i}. {activity.activity_name}\n"
            explanation += f"   Time: {activity.estimated_time} min | Priority: {activity.priority_level}\n"
            total_time += activity.estimated_time
        
        explanation += f"\nTotal Time Used: {total_time} minutes\n"
        explanation += f"Time Remaining: {self.available_minutes - total_time} minutes\n\n"
        
        explanation += f"SKIPPED ACTIVITIES ({len(self.skipped_activities)} tasks):\n"
        for i, activity in enumerate(self.skipped_activities, 1):
            if activity.completed:
                explanation += f"{i}. {activity.activity_name} (already completed)\n"
            else:
                explanation += f"{i}. {activity.activity_name}\n"
                explanation += f"   Time: {activity.estimated_time} min | Priority: {activity.priority_level}\n"
        
        return explanation
