def adicionar_linha(nome_arquivo, linha):
    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.writelines([linha])

adicionar_linha("2.txt", "Eu ganhei")