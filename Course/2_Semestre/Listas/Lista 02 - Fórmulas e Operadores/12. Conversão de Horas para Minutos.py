# Create a function that receives an amount of hours and returns the total in minutes.
def hours_to_minutes(h):
    minutes = h*60
    print(f"{h} hour(s) = {minutes} minute(s)")
    return minutes
hours_to_minutes(2)