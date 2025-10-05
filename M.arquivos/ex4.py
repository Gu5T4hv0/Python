def contar_linhas(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        reader = arquivo.readlines()
        contador = 0
        for linha in reader:
            contador += 1
        return contador

contar_linhas("2.txt")