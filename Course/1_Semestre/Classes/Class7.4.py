largura_sala = int(input("Qual a largura da sala, em cm: "))
comprimento_sala = int(input("Qual a comprimento da sala, em cm: "))
largura_piso = int(input("Qual a largura do piso, em cm: "))
comprimento_piso = int(input("Qual a comprimento do piso, em cm: "))
margem_de_erro = int(input("Qual a porcentagem de pisos a mais que você quer comprar: "))
percentual = (1 + (margem_de_erro/100))

area_sala = largura_sala * comprimento_sala
area_piso = largura_piso * comprimento_piso

total_de_pisos = (area_sala // area_piso)
total_com_margem = total_de_pisos * percentual

print(f"Voce vai precisar de {total_de_pisos} pisos, com margem de erros {total_com_margem}")