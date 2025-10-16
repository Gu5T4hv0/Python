def substituir(origem, substituido):
    with open(origem, "r", encoding="utf-8") as file:
        red = file.readlines()
        new_red = []
        for i in red:
            replace = i.replace("erro", "acerto")
            new_red.append(replace)

    with open(substituido, "w", encoding="utf-8") as file:
        file.writelines(new_red)
            
substituir("mensagem.txt", "mensagem_corrigida.txt")