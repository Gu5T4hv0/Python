nota_01 = float(input("Digite a 1° nota: "))
nota_02 = float(input("Digite a 2° nota: "))
media = (nota_01 + nota_02)/2

if media >= 7.0:
    print("APROVADO")
elif media >= 3.0:
    print("RECUPERAÇÃO")
elif media >= 2.0:
    print("PIX PRO PROF")
else:
    print("REPROVADO, SE LASCOU")