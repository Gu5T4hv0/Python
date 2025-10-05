mes = int(input("Digite o numero do mês"))

if (mes == 1):
    nome_do_mes = "Janeiro"
elif (mes == 2):
    nome_do_mes = "Fevereiro"
elif (mes == 3):
    nome_do_mes = "Março"
elif (mes == 4):
    nome_do_mes = "Abril"
elif (mes == 5):
    nome_do_mes = "Maio"
elif (mes == 6):
    nome_do_mes = "Junho"
elif (mes == 7):
    nome_do_mes = "Julho"
elif (mes == 8):
    nome_do_mes = "Agosto"
elif (mes == 9):
    nome_do_mes = "Setembro"
elif (mes == 10):
    nome_do_mes = "Outubro"
elif (mes == 11):
    nome_do_mes = "Novembro"
elif (mes == 12):
    nome_do_mes = "Dezembro"
else:
    nome_do_mes = "Não Existe"

print("O numero 3 é março")#estatico
print(f"O numero {mes} é {nome_do_mes}")#dinamico

print("O numero " + mes + " é " + nome_do_mes)#mais verboso

#f formata o formato da variavel ex.:(str para int)