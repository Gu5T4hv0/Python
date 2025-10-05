# Create a tuple with the 7 days of the week and allow the user to choose a number from 1 to 7 to display the corresponding day.
tuple = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

week_number = int(input("Type a number from 1 to 7 matching with a day of the week, and i will tell you the day: "))

real_week_number = week_number - 1

print(tuple[real_week_number])