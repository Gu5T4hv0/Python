# Create a function that receives the bases b1 and b2 and the height h of a trapeze and calculate its area:
def trapezium_area(b1, b2, h):
    a = (b1 + b2) * h/2
    print(f"The trapezio's area is {a}m²")
    return a
trapezium_area(2, 4, 3)