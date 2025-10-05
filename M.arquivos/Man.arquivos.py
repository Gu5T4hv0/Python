# dentro_do_arquivo = open("familia.txt", "r", encoding="utf-8")
# #vai abri o arquivo e vai acessar o que tem dentro
# linhas = dentro_do_arquivo.readlines()
# #abriu leu e criou uma lista e acoplou nessa variavel

# for linha in linhas:
#     print(linha)

# dentro_do_arquivo.close()
# #precisa fechar o arquivo


# with open("familia.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()

#     for _ in range(1000000000):
#         print(_)

#     for linha in linhas:
#         print(linha)


# with open("familia.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()

# linhas.append("\nEduarda Mendes")

# with open("familia.txt", "a", encoding="utf-8") as arquivo:
#     arquivo.writelines(["Só eu"])


# numeros = [1,2,3,4,5,6,7]
# numeros = [str(n) for n in numeros]
# with open("novo_arquivo.txt", "w") as arquivo:
#     arquivo.writelines(numeros)

# with open("words.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()

# total = 0
# for linha in linhas:
#     palavras = linha.split()
#     total += len(palavras)

# print(total)

# with open("words.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()

# maiores = 0
# for linha in linhas:
#     palavras = linha.split()
#     for palavra in palavras:
#         if len(palavras) <= 5:
#             maiores += 1

# print(maiores)