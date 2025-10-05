def contar_palavras(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as file:
        reader = file.read()
        words = reader.split()
        counter = 0
        for i in words:
            counter += 1
        print(counter)
        return counter

contar_palavras("9.txt")