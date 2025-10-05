print("With the formula (ax**2-bx-c=0) give me the following values")

a = int(input("Enter the a value:"))
b = int(input("Enter the b value:"))
c = int(input("Enter the c value:"))

delta = (b**2) - (4*a*c)

import math
raiz1 = (-b+math.sqrt(delta)) / (2*a)
raiz2 = (-b-math.sqrt(delta)) / (2*a)

print(f"The solutions are {raiz1} e {raiz2}")