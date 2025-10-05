def calcular_perimetro(mapa):
    linhas = len(mapa)
    colunas = len(mapa[0])
    perimetro = 0

    for i in range(linhas):
        for j in range(colunas):
            if mapa[i][j] == 'X':
                if i == 0 or mapa[i-1][j] == 'O':
                    perimetro += 1
                if i == linhas - 1 or mapa[i+1][j] == 'O':
                    perimetro += 1
                if j == 0 or mapa[i][j-1] == 'O':
                    perimetro += 1
                if j == colunas - 1 or mapa[i][j+1] == 'O':
                    perimetro += 1

    return f"Perímetro Total: {perimetro}"

mapa = [
    'XOOXO',
    'XOOXO',
    'OOOXO',
    'XXOXO',
    'OXOOO'
]

print(calcular_perimetro(mapa))