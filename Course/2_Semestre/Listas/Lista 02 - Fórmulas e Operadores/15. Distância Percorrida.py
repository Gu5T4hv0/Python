# Create a function that receives speed (m/s) and time (s) and calculate the distance traveled:
def distance_travelled(v, t):
    d = v * t 
    print(f"The distance travelled is {d}m")
    return d
distance_travelled(2, 3)