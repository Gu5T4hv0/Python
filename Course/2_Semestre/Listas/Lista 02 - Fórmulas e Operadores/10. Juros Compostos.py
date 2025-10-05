# Create a function that calculates the amount of a capital with compound interest:
def compound_interest_calculator(P, i, t):
    calc1 = 1 + i
    calc2 = calc1 ** t
    m = P * calc2
    print(f"{m:.2f}")
    return m
compound_interest_calculator(300, 0.10, 20)