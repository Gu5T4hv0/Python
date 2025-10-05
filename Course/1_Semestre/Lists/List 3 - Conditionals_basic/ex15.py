largura_da_sala = int(input("Digite a largura: "))
largura_do_piso = int(input("Digite a largura do piso: "))
comprimento_do_piso = int(input("Digite a comprimento do piso: "))

area_da_sala = largura_da_sala ** 2

area_do_piso = largura_do_piso * comprimento_do_piso

quantidade = area_da_sala / area_do_piso

print(quantidade)