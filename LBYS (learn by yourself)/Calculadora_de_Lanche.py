hamburguer = 0
cachorro_quente = 0
refrigerante = 0

print("Cardápio: \n1 - Hambúrguer: R$10 \n2 - Cachorro-quente: R$8 \n3 - Refrigerante: R$5")
numero = int(input("Digite o numero do lanche que desejas: "))
quantidade = int(input("Digite quantos desejas: "))

if numero == 1:
    hamburguer = quantidade * 10
elif numero == 2:
    cachorro_quente = quantidade * 8
elif numero == 3:
    refrigerante = quantidade * 5
else:
    print("Lanche não existente")

valor_total = hamburguer + cachorro_quente + refrigerante

print(f"Você escolheu {quantidade} vezes o item {numero}, logo o valor total a pagar é {valor_total}")