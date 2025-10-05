import random

numero_do_computador = random.randrange(1, 101)

continuar = True

while continuar:
    numero = int(input("Digite seu palpite: "))
    continuar = numero != numero_do_computador

    if continuar:
        print("Errou, tente novamente")
        contador += 1


print(f"Acertou, depois de {contador} vezes")