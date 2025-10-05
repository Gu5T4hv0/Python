def distancia_maxima(texto):
    posicoes = {}
    maior_distancia = -1
    letra_resultado = ''

    for i in range(len(texto)):
        letra = texto[i]
        if letra in posicoes:
            distancia = i - posicoes[letra][0]
            posicoes[letra][1] = distancia
            if distancia > maior_distancia:
                maior_distancia = distancia
                letra_resultado = letra
        else:
            posicoes[letra] = [i, 0]

    return letra_resultado + str(maior_distancia)

texto = "fffffahhhhhhaaahhhhbhhahhhhabxx"
print(distancia_maxima(texto))