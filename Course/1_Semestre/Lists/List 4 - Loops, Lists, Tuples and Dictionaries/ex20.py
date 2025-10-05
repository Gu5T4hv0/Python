# Read a list of 10 numbers and display even numbers.
numbers = []

for _ in range(10):
    number = int(input("Type a number: "))
    numbers.append(number)

for number in numbers:
    if number % 2 == 0:
        print(number)