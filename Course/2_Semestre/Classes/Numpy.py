#numpy é uma biblioteca feita em c para criar vetores e matrizes
# 1 dimensão = lista, array, vetor
# 2 dimensões = matriz
# tudo que uma lista faz o numpy faz numpy = performance
import numpy as np

vetor = np.array([2,3,4,5,6])
matriz = np.array([[2,4],[6,8]])

# impares = list(range(2, 11, 2))
print(vetor)
print(matriz)

#como crio a lista ultilizando numpy?

impares = np.arange(1,10,2)

np.random.randint
print(impares)