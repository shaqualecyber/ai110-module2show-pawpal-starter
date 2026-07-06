from dataclasses import dataclass


@dataclass
class PetProfile:
    """Represents a pet's profile with basic information."""
    pet_name: str
    species: str
    age: int
    health_notes: str

    def update_pet_info(self):
        """Update the pet's information."""
        pass

    def view_pet_details(self):
        """View the pet's details."""
        pass


class OwnerProfile:
    """Represents a pet owner's profile and preferences."""
    
    def __init__(self, owner_name: str, available_minutes: int, care_preferences: str):
        self.owner_name = owner_name
        self.available_minutes = available_minutes
        self.care_preferences = care_preferences

    def update_availability(self):
        """Update the owner's available time."""
        pass

    def update_preferences(self):
        """Update the owner's care preferences."""
        pass


@dataclass
class CareActivity:
    """Represents a care activity for the pet."""
    activity_name: str
    estimated_time: int
    priority_level: int
    completed: bool = False

    def edit_activity(self):
        """Edit the activity details."""
        pass

    def complete_activity(self):
        """Mark the activity as completed."""
        pass


class SchedulePlanner:
    """Manages and plans the pet's daily care schedule."""
    
    def __init__(self, activity_list: list, available_time: int):
        self.activity_list = activity_list
        self.available_time = available_time
        self.daily_schedule = []

    def build_schedule(self):
        """Build a daily schedule from available activities."""
        pass

    def prioritize_tasks(self):
        """Prioritize tasks based on importance and time."""
        pass

    def explain_schedule(self):
        """Explain the reasoning behind the schedule."""
        pass
