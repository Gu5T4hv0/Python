# Create a function that receives the coefficients a, b and c of a quadratic equation and calculate its roots using:
def bhaskara(a, b, c):
    delta = b **2 - 4*a*c
    bhask1 = (-b + delta**0.5)/(2*a)
    bhask2 = (-b - delta**0.5)/(2*a)
    print(bhask1, bhask2)
    return bhask1, bhask2
bhaskara(1, -3, -4)