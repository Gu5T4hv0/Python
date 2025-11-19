import numpy as np
vetor1 = np.arange(9)
vetor2 = np.arange(5,9)
vetor3 = np.arange(1,10,2)
print(vetor1, vetor2, vetor3)

# with open("notas.txt", "r") as arquivo:
#     notas = [int(nota.replace("\n", "")) for nota in arquivo.readlines()]
#     notas2 = []
#     for nota in arquivo.readlines():
#         nota_sem_barra_n = nota.replace("\n", "")
#         nota_int = int(nota_sem_barra_n)
#         notas2.append(nota_int)

matriz = np.arange(9).reshape(3,3)
print(matriz)

matriz_aleatoria = np.random.rand(3,3)
print(matriz_aleatoria)

yes = np.array2string(matriz_aleatoria, precision=2)
print(yes)

d = np.ravel(matriz)
print(d)