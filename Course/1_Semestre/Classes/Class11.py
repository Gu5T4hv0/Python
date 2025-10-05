frase = "O palmeiras vai jogar hoje"
palavras = frase.split(" ")

hashtag_1 = ""
indice = 0
if len(palavras[indice]) >= 5:
    hashtag_1 = f"#{palavras[indice].capitalize()}"

hashtag_2 = ""
indice = 1
if len(palavras[indice]) >= 5:
    hashtag_1 = f"#{palavras[indice].capitalize()}"

hashtag_3 = ""
indice = 2
if len(palavras[indice]) >= 5:
    hashtag_1 = f"#{palavras[indice].capitalize()}"

hashtag_4 = ""
indice = 3
if len(palavras[indice]) >= 5:
    hashtag_1 = f"#{palavras[indice].capitalize()}"

hashtag_5 = ""
indice = 4
if len(palavras[indice]) >= 5:
    hashtag_1 = f"#{palavras[indice].capitalize()}"


print(hashtag_1, hashtag_2, hashtag_3, hashtag_4, hashtag_5)