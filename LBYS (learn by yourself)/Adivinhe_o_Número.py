numero = int(input("Digite um numero entre 1 e 10: "))

valor_fixo = 7
if numero == valor_fixo:
    print("Você acertou o número!")
elif numero < valor_fixo and numero > 0:
    print("O número está um pouco acima!")
elif numero > valor_fixo and numero < 11:
    print("O número está um pouco abaixo!")
else:
    print("Número fora do intervalo permitido")