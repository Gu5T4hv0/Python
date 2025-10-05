import random
# def tresletras(palavra):
#     return palavra[0:3]

# def qtdVogais(palavra:str) -> int:
#     vogais = 'aeiou'
#     qtd = 0
#     for letra in palavra.lower():
#         if letra in vogais:
#             qtd += 1

#     return qtd

# def listaAleatoria(qtd, range_inicial, range_final) -> list:
#     lista = []
#     for _ in range(qtd):
#         aleatorio = random.randrange(range_inicial, range_final+1)
#         lista.append(aleatorio)
#     return lista

def sequencia(inicial:int, final:int, passo = 1) -> list:
    lista = []
    for i in range(inicial, final+1, passo):
        lista.append(i)
    return lista