number1 = int(input("Type the number1: "))
number2 = int(input("Type the number2: "))
number3 = int(input("Type the number3: "))

if number1 > number2 and number1 > number3:
    print(number1, "is the greatest number")
elif number2 > number1 and number2 > number3:
    print(number2, "is the greatest number")
elif number3 > number2 and number3 > number1:
    print(number3, "is the greatest number")
else:
    print("There is no greater number")