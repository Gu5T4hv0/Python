# def criar_matriz_3x3(): → Cria uma matriz 3x3 com números de 1 a 9.
def criar_matriz_3x3():
    return [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
# def soma_matriz(matriz): → Retorna a soma de todos os elementos.
def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma
# def maior_menor_matriz(matriz): → Retorna o maior e menor valor.
def maior_menor_matriz(matriz):
    maior = matriz[0][0]
    menor = matriz[0][0]

    for linha in matriz:
        for valor in linha:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor

    return (maior, menor)
# def diagonal_principal(matriz): → Retorna a diagonal principal.
def diagonal_principal(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    return diagonal
# def diagonal_secundaria(matriz): → Retorna a diagonal secundária.
def diagonal_secundaria(matriz):
    n = len(matriz)
    diagonal = []
    for i in range(n):
        diagonal.append(matriz[i][n - 1 - i])
    return diagonal
# def transposta(matriz): → Retorna a transposta da matriz.
def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = []

    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        resultado.append(nova_linha)

    return resultado
# def matriz_simetrica(matriz): → Verifica se a matriz é simétrica.
def matriz_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
# def multiplicar_matriz(matriz, fator): → Multiplica todos os elementos por um fator.
def multiplicar_matriz(matriz, fator):
    resultado = []
    for linha in matriz:
        nova_linha = []
        for valor in linha:
            nova_linha.append(valor * fator)
        resultado.append(nova_linha)
    return resultado
# def contar_pares_matriz(matriz): → Conta quantos pares existem na matriz.
def contar_pares_matriz(matriz):
    contador = 0
    for linha in matriz:
        for valor in linha:
            if valor % 2 == 0:
                contador += 1
    print(contador)
    return contador
# def matriz_identidade(n): → Retorna uma matriz identidade de ordem n.
def matriz_identidade(n):
    identidade = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        identidade.append(linha)
    return identidade
# def soma_linhas(matriz): → Retorna a soma de cada linha.
def soma_linhas(matriz):
    soma = []
    for linha in matriz:
        soma.append(sum(linha))
    return soma
# def soma_colunas(matriz): → Retorna a soma de cada coluna.
def soma_colunas(matriz):
    colunas = len(matriz[0])
    linhas = len(matriz)
    somas = []

    for j in range(colunas):
        soma = 0
        for i in range(linhas):
            soma += matriz[i][j]
        somas.append(soma)
    return somas
# def contem_valor(matriz, valor): → Verifica se o valor está presente.
def contem_valor(matriz, valor):
    for linha in matriz:
        if valor in linha:
            return True
    return False
# def substituir_negativos(matriz): → Substitui todos os negativos por zero.
def substituir_negativos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < 0:
                matriz[i][j] = 0
    return matriz
# def matriz_aleatoria(linhas, colunas): → Cria uma matriz com números aleatórios entre 0 e 100.
import random

def matriz_aleatoria(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            linha.append(random.randint(0, 100))
        matriz.append(linha)
    return matriz