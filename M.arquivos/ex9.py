def remover_linhas_vazias(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as file:
        reader = file.readlines()
        new_text = []
        for line in reader:
            if line != '\n':
                new_text.append(line)
                
    with open("4.1.txt", "w", encoding="utf-8") as new_file:
        for newline in new_text:
            new_file.write(newline)

remover_linhas_vazias("4.txt")