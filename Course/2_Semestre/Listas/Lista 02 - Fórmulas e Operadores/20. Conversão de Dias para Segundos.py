# Create a function that receives a number of days and returns the total of seconds.
def days_to_seconds(d):
    seconds = d * 86400
    print(f"{d} days has {seconds} seconds")
days_to_seconds(3)