texto = "fffffahhhhhhaaahhhhbhhahhhhabxx"

posicoes = {}

for indice, letra in enumerate(texto):
    if letra not in posicoes:
        posicoes[letra] = [indice]
    else:
        posicoes[letra].append(indice)

letra_max = ''
distancia_max = -1

for letra in texto:
    indices = posicoes[letra]
    distancia = indices[-1] - indices[0]

    if distancia > distancia_max:
        distancia_max = distancia
        letra_max = letra

print(f"{letra_max}{distancia_max}")