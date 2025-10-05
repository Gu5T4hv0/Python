# Write a program that displays all the divisors of a number provided by the user.
number = int(input("Type a number and I will give you all your divisors: "))

divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(f"The divisors of {number} are {divisors}")