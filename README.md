# 🧠 HabitForge - Habit Tracker CLI App

HabitForge is a simple, user-friendly command-line application that helps users track their daily and weekly habits using Python. It follows object-oriented and functional programming principles and persists habit data using a JSON file.

---

## 📦 Features

- Add custom or preset habits
- Track daily or weekly completions
- Mark habits as done for today
- View current and longest streaks
- List all tracked habits
- JSON-based persistent storage

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **OOP** (Object-Oriented Programming)
- **Functional Programming** (for analytics)
- **Click** (Command-line interface)
- **JSON** (for data persistence)

---

## 🧩 Project Structure

```bash
├── habit.py           # Defines the Habit class and handles JSON loading/saving
├── analytics.py       # Contains habit analytics functions (streaks, filtering)
├── main.py            # Command-line interface using Click
├── habits.json        # Data file where all habit info is stored
├── README.md          # You're reading it 😄
```

---

## 📄 JSON Data Structure (habits.json)

Each habit in the file looks like this:

```json
{
  "name": "Drink Water",
  "frequency": "daily",
  "description": "Stay hydrated",
  "completions": [
    "2025-07-01",
    "2025-07-02",
    ...
  ]
}
```

- `name`: Name of the habit (string)
- `frequency`: Either `daily` or `weekly`
- `description`: (Optional) A short description of the habit
- `completions`: List of dates (as strings) when the habit was completed (format: `YYYY-MM-DD`)

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install click
```

### 2. Run the app

```bash
python main.py [COMMAND]
```

### Example commands:

```bash
python main.py add          # Add a new habit
python main.py list         # List all habits
python main.py done         # Mark a habit as done
python main.py streak       # View streaks
```

---

## 📌 Notes

- The habit streak logic adapts to frequency (daily = every day, weekly = every 7 days).
- All data is saved to `habits.json` and retained between runs.

---

## 📚 Future Improvements

- Add reminders/notifications
- Track missed days explicitly
- Web or GUI frontend
- Database support (SQLite/PostgreSQL)

---

