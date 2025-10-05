matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# lista dentro da lista
# matriz 3 por 3

# # iterando na lista
# for linha in matriz:
#     for valor in linha:
#         print(valor, end=" ")
#     print()
# #acima - for aninhados (um dentro do outro)- produto cartesiano (perde performance)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()