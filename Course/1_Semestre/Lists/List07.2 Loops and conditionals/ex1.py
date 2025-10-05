# Make an algorithm that receives an integer, representing a quantity in seconds and displays a text stating the total of days, hours, minutes and seconds, when there is one of these.
time = 3662

days = time // 86400
time = time % 86400

hours = time // 3600
time = time % 3600

minutes = time // 60

seconds = time % 60

result = []

if days == 1:
    result.append(f"{days} day")
elif days > 1:
    result.append(f"{days} days")

if hours == 1:
    result.append(f"{hours} hour")
elif hours > 1:
    result.append(f"{hours} hours")

if minutes == 1:
    result.append(f"{minutes} minute")
elif minutes > 1:
    result.append(f"{minutes} minutes")

if seconds == 1:
    result.append(f"{seconds} second")
elif seconds > 1 or (seconds == 0 and len(result) == 0):
    result.append(f"{seconds} seconds")

output = ', '.join(result)

print(output)
