# Make a program that reads a number and displays its multiplication table (1 to 10).
number = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")