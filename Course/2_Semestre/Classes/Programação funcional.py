from functools import reduce
lista_original = [5, 10, 15, 20, 25]
print(lista_original)


mapeado = list(map(lambda x: x * 2, lista_original))
print(mapeado)

filtrado = list(filter(lambda x: x > 15, lista_original))
print(filtrado)

reduzido = reduce(lambda x, y: x + y, lista_original)
print(reduzido)#acumula