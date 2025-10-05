# Create a program that reads multiple numbers until the user enters 0 and shows the sum of the numbers read.
numbers = []
number = 1
while number != 0:
    number = int(input("Type a number: "))
    if number != 0:
        numbers.append(number)
        
summing = sum(numbers)

print(summing)