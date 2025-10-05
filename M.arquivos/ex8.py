def buscar_palavra(nome_arquivo, palavra):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        reader = arquivo.readlines()
        return reader.count(palavra)

buscar_palavra("2.txt", "Sed")