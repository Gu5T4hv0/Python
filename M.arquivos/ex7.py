def exibir_com_numeracao(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        reader = arquivo.readlines()
        for i, linha in enumerate(reader, start=1):
            print(f"{i}: {linha.strip()}")

exibir_com_numeracao("2.txt")