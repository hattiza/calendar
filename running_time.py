import datetime

# Prompt the user for tasks, day of the week, start time, and end time
tasks = input("Enter the tasks you do during the day: ")

# Get the current date
current_date = datetime.date.today()

# Calculate the running total for each day for the next 100 days
running_sum = 0
for i in range(365):
    # Get the current day of the week
    day_of_week = current_date.strftime("%A")

    # Calculate the free hours based on the day of the week
    if day_of_week == "Saturday" or day_of_week == "Sunday":
        free_hours = 6
    else:
        free_hours = 2

    running_sum += free_hours
    # Print the running total for the current day
    print(f"{current_date}: {free_hours} {running_sum}")

    # Increment the current date by one day
    current_date += datetime.timedelta(days=1)