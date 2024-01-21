import calendar
import datetime

def day_of_week(day, month, year):
    try:
        # Check for a future year
        current_year = datetime.datetime.now().year
        if year > current_year:
            print(f"Oh, planning ahead, are we? Best of luck with the time travel to {year}!")

        # Check for valid month input
        if not 1 <= month <= 12:
            raise ValueError("Oh, a creative month choice! Unfortunately, we're stuck with the boring 12 months.")

        # Check for valid day input based on the month
        max_days_in_month = calendar.monthrange(year, month)[1]
        if not 1 <= day <= max_days_in_month:
            raise ValueError(f"Wow, you've discovered a secret day in {calendar.month_name[month]}! "
                             f"Hint: It only has {max_days_in_month} days.")

        # Calculate and return the day of the week
        return calendar.day_name[calendar.weekday(year, month, day)]

    except ValueError as e:
        print(f"Well, well, well... {e}")
        return None  # Return None to indicate an error


# Take input from the user
try:
    day = int(input("Enter the day (1-31): "))
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year (e.g., 2024): "))
    
    # Assuming it's being referred to 21st century itself
    if year < 100:
        year += 2000


    # Get the day of the week or handle exceptions
    day_name = day_of_week(day, month, year)

    # If there was an error, don't print the day of the week
    if day_name is not None:
        print(f"The day of the week for {day:02d}-{month:02d}-{year} is {day_name}.")

except ValueError as e:
    pass  # Do nothing here since the error message is already printed within the function
