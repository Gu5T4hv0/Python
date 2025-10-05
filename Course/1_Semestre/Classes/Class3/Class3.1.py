nascimento = int(input("Digite o ano em que nasceu: "))

idade = 2025 - nascimento

if idade >= 60:
    print("idoso")
elif idade >= 18:
    print("adulto")
elif idade >= 12:
    print("adolescente")
elif idade >= 2:
    print("criança")
else:
    print("bebê")