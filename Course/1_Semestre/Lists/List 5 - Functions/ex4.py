# Create a function called "power_calculator" that receives two numbers as arguments: the base and the exponent. A function must return the base high to the exponent
def power_calculator(a, b: int) -> int:
    power = a ** b
    return power

power_calculator(2, 3)