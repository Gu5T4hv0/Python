# Make a program that reads 10 numbers and create a new list only with those who are greater than 50.
numbers = []
for i in range(10):
    number = int(input("Type a number: "))
    if number > 50:
        numbers.append(number)

print(numbers)