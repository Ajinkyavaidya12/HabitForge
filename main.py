# main.py
# This script provides the command-line interface using click

import click
from habit import Habit, temp_loaded_habits
from analytics import list_all, find_streak_for, find_longest_streak, find_max_streak_for

# Load habits at program start
habits = Habit.load_habits()
temp_loaded_habits.clear()
temp_loaded_habits.extend(habits)

@click.group()
def cli():
    """HabitForge - A habit tracker CLI app"""
    pass

@cli.command()
def list():
    """Show all habits stored"""
    for h in temp_loaded_habits:
        click.echo(f"{h.name} ({h.frequency}) - {len(h.completions)} times")

@cli.command()
@click.option('--preset', is_flag=True, help='Choose from preset habits')
def add(preset):
    """Add a new habit (custom or preset)"""
    if preset:
        # Show preset options
        options = [
            ("Brush Teeth", "daily", "Morning hygiene routine"),
            ("Drink Water", "daily", "Stay hydrated"),
            ("Practice Gratitude", "daily", "Write down 3 things you're grateful for"),
            ("Declutter Closet", "weekly", "Organize and clean your wardrobe"),
            ("Weekly Journal", "weekly", "Reflect on the week")
        ]
        for i, (n, f, _) in enumerate(options, 1):
            click.echo(f"{i}. {n} ({f})")
        choice = click.prompt("Pick a habit", type=int)
        name, freq, desc = options[choice - 1]
    else:
        # Custom habit input
        name = click.prompt("Habit name")
        freq = click.prompt("Frequency (daily/weekly)")
        desc = click.prompt("Description", default="")
    
    h = Habit(name, freq, description=desc)
    h.save()
    click.echo(f"Added habit: {h.name}")

@cli.command()
def done():
    """Mark one habit as completed for today"""
    for i, h in enumerate(temp_loaded_habits, 1):
        click.echo(f"{i}. {h.name} ({h.frequency})")
    choice = click.prompt("Which habit to mark as done", type=int)
    habit = temp_loaded_habits[choice - 1]
    habit.mark_completed()
    click.echo(f"Marked '{habit.name}' as complete")

@cli.command()
def streak():
    """View current and longest streaks"""
    click.echo("1. Longest streak overall")
    click.echo("2. View streak for a habit")
    sub = click.prompt("Choose option", type=int)

    if sub == 1:
        name, count = find_longest_streak(temp_loaded_habits)
        if name:
            click.echo(f"Longest streak is for '{name}' with {count} days")
        else:
            click.echo("No data yet.")
    elif sub == 2:
        for i, h in enumerate(temp_loaded_habits, 1):
            click.echo(f"{i}. {h.name}")
        choice = click.prompt("Pick a habit", type=int)
        habit = temp_loaded_habits[choice - 1]
        current = find_streak_for(temp_loaded_habits, habit.name)
        longest = find_max_streak_for(temp_loaded_habits, habit.name)
        click.echo(f"Current streak: {current}")
        click.echo(f"Longest streak: {longest}")
    else:
        click.echo("Invalid option")

if __name__ == '__main__':
    cli()
