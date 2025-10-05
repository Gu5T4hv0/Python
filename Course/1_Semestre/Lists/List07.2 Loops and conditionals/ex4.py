# Give a 3x3 matrix filled with integers and print the sum of the elements of the main diagonal.
def diagonal_principal(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    summer = sum(diagonal)
    return summer

diagonal_principal([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6]])