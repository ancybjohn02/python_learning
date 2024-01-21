import calendar

def day_of_week(day, month, year):
    return calendar.day_name[calendar.weekday(year, month, day)]

# Input
day = int(input("Enter the day (1-31): "))
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year (eg. 2024): "))

# Day
day_name = day_of_week(day, month, year)

print(f"The day of the week for {day:02d}-{month:02d}-{year} is {day_name}.")
