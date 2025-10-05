# Create a function that receives the radius of a sphere and calculates its volume:
import math
def volume_sphere(r):
    v = (4/3) * math.pi * r ** 3
    print(f"The volume of the sphere is {v:.2f} m³")
    return v
volume_sphere(4)