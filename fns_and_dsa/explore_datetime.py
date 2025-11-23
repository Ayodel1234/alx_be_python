from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time in a variable
    current_date = datetime.now()

    # Format the date and time in YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("Current date and time:", formatted_date)

    # Return current_date in case the main program needs it
    return current_date


def calculate_future_date(current_date, days_to_add):
    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)

    # Format the date as YYYY-MM-DD
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print("Future date:", formatted_future_date)

    # Return future_date if needed
    return future_date


def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Ask user for number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
