lista = []
ordem = ""
while ordem != "sair":
    ordem = str(input("Digite um nome: "))
    if ordem != "sair":
        lista.append(ordem)

print(lista)