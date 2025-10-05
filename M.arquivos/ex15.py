def inverter_linhas(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        linhas.sort(reverse=True, key=lambda linha: linha.lower())
        
        linhas_strip = []
        for linha in linhas:
            linhas_strip.append(linha.strip())
        linhas = linhas_strip

    with open("6.txt", "w", encoding="utf-8") as novo_arquivo:
        for linha in linhas:
            novo_arquivo.write(linha + "\n")
inverter_linhas("2.txt")