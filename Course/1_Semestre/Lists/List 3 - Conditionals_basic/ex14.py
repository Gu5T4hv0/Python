bit1 = int(input("Digite o bit 1: "))
bit2 = int(input("Digite o bit 2: "))
bit3 = int(input("Digite o bit 3: "))
bit4 = int(input("Digite o bit 4: "))
bit5 = int(input("Digite o bit 5: "))

decimal = (bit1 * (2 ** 4)) + (bit2 * (2 ** 3)) + (bit3 * (2 ** 2)) + (bit4 * (2 ** 1)) + (bit5 * (2 ** 0))

print(decimal)