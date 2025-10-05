def comparar_numeros():
    number1 = float(input("Give me the first number: "))
    number2 = float(input("Give me the second number: "))
    if number1 > number2:
        print(f"{number1} is higher than {number2}")
    else:
        print(f"{number1} is lower than {number2}")
comparar_numeros()

def verificar_tres_iguais(n1, n2, n3):
    if (n1 == n2) and (n2 == n3):
        print("The numbers are all equal")
    else:
        print("There is some different number between them")
verificar_tres_iguais(3, 3, 3)

def operacoes_booleanas(b1, b2):
    e = b1 and b2
    ou = b1 or b2
    nao1 = not b1
    nao2 = not b2
    print(f"{b1} AND {b2} = {e}\n {b1} OR {b2} = {ou}\n NOT {b1} = {nao1}\n NOT {b2} = {nao2}")
operacoes_booleanas(True, False)

def verificar_idade_entre():
    age = int(input("How old are you? "))
    if age >= 18 and age <= 30:
        print("You can enter")
    else:
        print("You're not allowed")
verificar_idade_entre()