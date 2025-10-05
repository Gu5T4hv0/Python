def linhas_com_palavra(nome_arquivo, palavra):
    with open(nome_arquivo, "r", encoding="utf-8") as file:
        reader = file.readlines()
        lines = []
        for line in reader:
            if palavra in line:
                lines.append(line)
        return lines

linhas_com_palavra("9.txt", "chuva")