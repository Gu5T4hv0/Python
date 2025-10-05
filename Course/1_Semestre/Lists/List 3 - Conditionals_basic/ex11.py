nascimento = int(input("Digite o ano em que nasceu: "))

idade = 2025 - nascimento

if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 19:
    print("Adolescente")
elif 20 <= idade <= 35:
    print("Jovem adulto")
elif 36 <= idade <= 60:
    print("Adulto")
else:
    print("Idade não catálogavel")