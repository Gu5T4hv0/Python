def inserir(origem, adicionado):
    with open(origem, "r", encoding="utf-8") as file:
        lido = file.read()
    with open(adicionado, "a", encoding="utf-8") as file:
        file.write(f"\n{lido}")
inserir("basetext.txt", "anotacoes.txt")