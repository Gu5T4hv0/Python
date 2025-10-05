def caixa_eletronico(saque, cedulas):
    total = 0
    for value, quantity in cedulas.items():
        total += value * quantity
    
    if total < saque:
        print("Impossible")
    cedulas = {100:2, 50:1, 20:5, 10:10}
    menor_cedula = min(cedulas)
    if saque % menor_cedula != 0:
        print("Impossible")
    print(total, menor_cedula)

caixa_eletronico(280, {100:2, 50:1, 20:5, 10:10})