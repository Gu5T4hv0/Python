# Create a function called "calculate_discount" that receives the value of a product and a percentage of discount as arguments, and returns the product value with the discount applied.
def calculate_discount(value, discount):
    calculator = (discount * value) / 100
    print(calculator)
    return calculator

calculate_discount(300, 20)