def ler_arquivo(nome_arquivo):
    with open("2.txt", "r", encoding="utf-8") as arquivo:
        return arquivo.read()

ler_arquivo("2.txt")