# daily_reminder.py

# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority description
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' is a task with unspecified priority"

# Time-bound modification
if time_bound == "yes":
    print(f"\nReminder: {base_message} that requires immediate attention today!")
else:
    print(f"\nNote: {base_message}. Consider completing it when you have free time.")
