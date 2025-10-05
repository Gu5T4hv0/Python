# def imprimir():
#     print("oi")

# imprimir()

# def imprimir(texto):
#     print(texto)

def abreviar(nome: str) -> str:
    palavras = nome.split(" ")
    resultado = ""
    for palavra in palavras:
        resultado += palavra[0]
    return resultado.lower()

