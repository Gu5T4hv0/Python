def remover_palavra(nome_arquivo, palavra_antiga, palavra_nova):
    with open(nome_arquivo, "r", encoding="utf-8") as file:
        reader = file.read()
        spliter = reader.split()
        new_text = []
        for line in spliter:
            if line == palavra_antiga:
                new_text.append(palavra_nova)
            else:
                new_text.append(line)
        joiner = " ".join(new_text)
        print(joiner)
    with open(nome_arquivo, "w", encoding="utf-8") as new_file:
        new_file.write(joiner)

remover_palavra("8.txt", "esperança", "fé")