def saudacao_usuario(nome, idade):
    print(f"Olá {nome}, você tem {idade} anos.")
saudacao_usuario("Arthur", "19")

def soma_dois_numeros():
    number1 = int(input("Give me one number:"))
    number2 = int(input("Give me another number:"))
    result = number1 + number2
    print(f"The sum is: {result}")
soma_dois_numeros()

def mostrar_preco_produto(nome, preço):
    print(f"O produto {nome} custa R$ {preço}")
mostrar_preco_produto("sabonete", 3)

def converter_metros_para_centimetros():
    meters = int(input("How many meters has the object in front of you?"))
    centimeters = meters*100
    print(f"This value ({meters}m) in centimeters is {centimeters}cm")
converter_metros_para_centimetros()

def mostrar_altura_peso():
    height = input("What is your height?")
    weight = input("What ir your weight?")
    print(f"Sua altura é {height} m e seu peso é {weight} kg.")
mostrar_altura_peso()