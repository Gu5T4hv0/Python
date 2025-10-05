def contar_ocorrencias(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read().lower()
        resultado = {}
        spliter = texto.split()
        for palavra in spliter:
            if palavra in resultado:
                resultado[palavra] += 1
            else:
                resultado[palavra] = 1
        return resultado

contar_ocorrencias("2.txt")