#Crie um programa que leia 5 nomes e armazene em uma lista. Depois, exiba-os em ordem alfabética.
nomes = []

for _ in range(5):
    nome = input(f"Digite o {_ + 1}º nome: ")
    nomes.append(nome)

nomes.sort()
print(nomes)