# Create a function that receives mass (kg) and acceleration (m/s 2) and calculate the force:
def calculate_strength(m,a):
    f = m * a
    print(f"{f}N")
    return f
calculate_strength(3,5)