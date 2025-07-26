# analytics.py
# This module provides analytics functions for habit tracking.

from typing import List
from habit import Habit

def list_all(habits: List[Habit]) -> List[str]:
    """Return a list of all habit names."""
    names = []
    for h in habits:
        names.append(h.name)
    return names

def list_by_freq(habits: List[Habit], freq: str) -> List[str]:
    """Return all habits matching a given frequency (daily/weekly)."""
    matched = []
    for h in habits:
        if h.frequency == freq:
            matched.append(h.name)
    return matched

def find_longest_streak(habits: List[Habit]):
    """
    Find the habit with the longest current streak.
    Returns: (habit_name, streak_count)
    """
    longest_name = None
    longest_streak = 0
    for h in habits:
        streak = h.get_streak()
        if streak > longest_streak:
            longest_streak = streak
            longest_name = h.name
    return longest_name, longest_streak

def find_streak_for(habits: List[Habit], name: str) -> int:
    """Return the current streak for a specific habit by name."""
    for h in habits:
        if h.name == name:
            return h.get_streak()
    return 0

def find_max_streak_for(habits: List[Habit], name: str) -> int:
    """Return the all-time longest streak for a specific habit by name."""
    for h in habits:
        if h.name == name:
            return h.get_max_streak()
    return 0
