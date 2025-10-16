def copiar_arquivo(origem):
    with open(origem, "r", encoding="utf-8") as file:
        lido = file.read()
    with open("copied.txt", "w", encoding="utf-8") as file:
        file.write(lido)

copiar_arquivo("copy.txt")