def escrever_texto(nome_arquivo, texto):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        return arquivo.write(texto)


escrever_texto("1.txt", "I like pizza")