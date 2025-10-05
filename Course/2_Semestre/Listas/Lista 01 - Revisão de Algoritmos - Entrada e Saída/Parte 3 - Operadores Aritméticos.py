def operacoes_basicas():
    number1 = input("Give the first number: ")
    number2 = input("Give the second number: ")
    n1 = float(number1)
    n2 = float(number2)
    summing = n1 + n2
    subtract = n1 - n2
    multiply = n1 * n2
    divide = n1 / n2
    print(f"The sum is {summing}, the difference is {subtract}, the multiplication is {multiply}, the division is {divide}")
operacoes_basicas()

def potencia_e_raiz():
    number = int(input("Give me a number: "))
    square = number ** 2
    root = number ** 0.5
    print(f"The square of this number is {square}. And the root is {root:.2f}")
potencia_e_raiz()

def aplicar_desconto(value):
    percentage = 10
    result = (percentage / 100) * value
    print(f"The tithe of {value} is {result}")
aplicar_desconto(300)

def resto_divisao():
    number1 = float(input("Give me the first number: "))
    number2 = float(input("Give me the second number: "))
    result = number1 % number2
    print(f"The rest of the division of the first number by the second one is {result}")
resto_divisao()