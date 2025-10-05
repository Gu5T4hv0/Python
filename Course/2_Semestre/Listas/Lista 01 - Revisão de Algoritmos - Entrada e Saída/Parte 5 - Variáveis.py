def informacoes_pessoais(name, age, city):
    print(f"My name is {name}, I'm {age} years old and I live in {city} in vacation.")
informacoes_pessoais("Arthur", 19, "BH é nóis")

def dobrar_valor():
    number = int(input("Gimme a number: "))
    double = number * 2
    print(f"The double of your number is {double}")
dobrar_valor()

def variaveis_dependentes():
    first = 10
    second = first + 5
    print(f"The first number was {first}, and the second is {second}")
variaveis_dependentes()