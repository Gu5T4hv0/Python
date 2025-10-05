# Make a program that displays all the odd numbers from 1 to a number given by the user.
number = int(input("Type a number: "))

odd_numbers = []
for i in range(number):
    i += 1
    if i % 2 != 0:
        odd_numbers.append(i)

for i in odd_numbers:
    print(i)