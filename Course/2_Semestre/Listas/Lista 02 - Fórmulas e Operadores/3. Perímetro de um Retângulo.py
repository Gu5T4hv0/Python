# Create a function that takes the length and width of a rectangle and calculates its perimeter:
def perimeter_rectangle(c, l):
    calc = c + l
    perimeter = 2 * calc
    return f"The perimetro is {perimeter}"
print(perimeter_rectangle(2, 3))