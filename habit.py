# habit.py
# This module defines the Habit class and handles JSON file interactions.

import json
from datetime import datetime, timedelta
from typing import List, Optional

# Global cache used to store currently loaded habits
temp_loaded_habits = []

class Habit:
    def __init__(self, name: str, frequency: str, completions: Optional[List[str]] = None, description: str = ""):
        self.name = name
        self.frequency = frequency
        self.description = description
        self.completions = completions if completions else []

    def mark_completed(self):
        """Add today's date to completions if not already added."""
        now = datetime.now().strftime('%Y-%m-%d')
        if now not in self.completions:
            self.completions.append(now)
            Habit.save_all(temp_loaded_habits)  # persist changes

    def is_due_today(self):
        """Return True if the habit is due today based on last completion and frequency."""
        if not self.completions:
            return True
        last = datetime.strptime(self.completions[-1], '%Y-%m-%d')
        today = datetime.now()
        delta = timedelta(days=1 if self.frequency == 'daily' else 7)
        return (today - last).days >= delta.days

    def get_streak(self):
        """Calculate current streak based on most recent completions."""
        dates = sorted([datetime.strptime(d, '%Y-%m-%d') for d in self.completions], reverse=True)
        streak = 0
        today = datetime.now()
        delta = timedelta(days=1 if self.frequency == 'daily' else 7)

        for i, d in enumerate(dates):
            if i == 0:
                if (today - d).days > delta.days:
                    break
            elif (dates[i - 1] - d).days != delta.days:
                break
            streak += 1
        return streak

    def get_max_streak(self):
        """Find the longest continuous streak in all completions."""
        dates = sorted([datetime.strptime(d, '%Y-%m-%d') for d in self.completions])
        if not dates:
            return 0
        max_streak = 1
        current_streak = 1
        delta = timedelta(days=1 if self.frequency == 'daily' else 7)

        for i in range(1, len(dates)):
            if (dates[i] - dates[i - 1]).days == delta.days:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1
        return max_streak

    def to_dict(self):
        """Convert Habit object to dictionary (used for saving)."""
        return {
            'name': self.name,
            'frequency': self.frequency,
            'description': self.description,
            'completions': self.completions
        }

    @staticmethod
    def from_dict(data):
        """Convert dictionary to Habit object (used for loading)."""
        return Habit(
            data['name'],
            data['frequency'],
            data.get('completions', []),
            data.get('description', "")
        )

    @staticmethod
    def load_habits():
        """Load all habits from the habits.json file."""
        try:
            with open('habits.json', 'r') as f:
                data = json.load(f)
                return [Habit.from_dict(h) for h in data]
        except FileNotFoundError:
            return []

    def save(self):
        """Save or update the current habit in the global list and file."""
        for i, h in enumerate(temp_loaded_habits):
            if h.name == self.name:
                temp_loaded_habits[i] = self
                break
        else:
            temp_loaded_habits.append(self)
        Habit.save_all(temp_loaded_habits)

    @staticmethod
    def save_all(habits: List['Habit']):
        """Save all habits to the JSON file."""
        with open('habits.json', 'w') as f:
            json.dump([h.to_dict() for h in habits], f, indent=4)
