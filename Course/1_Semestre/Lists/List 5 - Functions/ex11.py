# Create a function called square that receives two parameters, one for the base and another for the height show a square made by asterisks.
def square(a, b):
    for _ in range(b):
        print("*"* a)

square(5, 3)