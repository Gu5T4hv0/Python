def soma(a, b):
    return a + b

def triplo(numero: int) -> int:
    return numero * 3

def nickname(nome: str) -> str:
    palavras = nome.lower().split(" ")
    letras = []
    quantidade = []
    for palavra in palavras:
        letras.append(palavra[0])
        quantidade.append(str(len(palavra)))
    
    return "".join(letras) + "".join(quantidade)

def soPares(numeros: list) -> list:
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares

