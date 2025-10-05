lado1 = 0
lado2 = 9
lado3 = 4

if lado1 == lado2 == lado3:
    print("Equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Iscóceles")
else:
    print("Escaleno")