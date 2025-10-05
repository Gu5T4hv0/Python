# MEU

# with open("words.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()

# contagem = {}
# repetidas = 0
# for linha in linhas:
#     palavras = linha.split()
#     for palavra in palavras:
#         palavra = palavra.lower()
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1

# for quantidade in contagem.values():
#     if quantidade > 1:
#         repetidas += 1

# print(repetidas)


# DUDA (quantas repetições existem)

with open("words.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

unicas = []
contador = 0
for linha in linhas:
    palavras = linha.lower().split()
    for palavra in palavras:
        if palavra in unicas:
            contador += 1
        else:
            unicas.append(palavra)

print(f"Existem {contador} palavras repetidas")


# criptografar
# with open("words.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()

# consoantes = "bcdfghjklmnpqrstvwxyz"
# vogais = 'aeiou'

# for linha in linhas:
#     cripfografado = ""
#     for letra in linha:
#         if letra in consoantes.upper():
#             cripfografado += "@"
#         elif letra in consoantes:
#             cripfografado += "*"
#         elif letra in vogais.upper():
#             cripfografado += "#"
#         elif letra in vogais:
#             cripfografado += "$"
#         else:
#             cripfografado += letra


# with open("words.txt", "r", encoding="utf-8") as arquivo:
#     arquivo.write(cripfografado)