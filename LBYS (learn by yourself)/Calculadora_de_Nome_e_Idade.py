nome = input("Digite seu nome:")
idade = int(input("Digite sua idade: "))

if idade < 100:
    quanto_falta = 100 - idade
    print(f"Olá, {nome.upper()}! Faltam {quanto_falta} anos para você completar 100 anos.")
else:
    print(f"Olá, {nome.upper()}! Você já passou dos 100 anos!")