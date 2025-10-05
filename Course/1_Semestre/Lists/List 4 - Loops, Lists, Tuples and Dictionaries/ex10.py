# Write a program that calculates the factorial of a number using loop for.
import math
number = int(input("Type a number and I will give you the factorial! "))

numbers = []
for i in range(number):
    i += 1
    numbers.append(i)

result = math.prod(numbers)
print(result)