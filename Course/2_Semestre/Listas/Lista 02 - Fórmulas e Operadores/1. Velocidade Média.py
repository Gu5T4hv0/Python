# Create a function that receives the distance traveled (in meters) and time spent (in seconds) and calculate the average speed using the formula:
def calculate_velocity(d, t):
    v = d/t
    print(f"The velocity is {v}km/h")
    return v

calculate_velocity(12, 6)