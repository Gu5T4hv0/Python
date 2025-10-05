import datetime

def calcular_idade(ano_de_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_de_nascimento
    print(f"Você tem {idade} anos.")

ano_de_nascimento = int(input("Digite o ano em que você nasceu: "))
calcular_idade(ano_de_nascimento)