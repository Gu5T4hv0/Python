# Create a function that calculates the simple interest of a capital P with rate i over time t:
def simple_interest_calculator(P, i, t):
    j = P * i * t
    print(j)
    return j
simple_interest_calculator(300, 0.10, 20)