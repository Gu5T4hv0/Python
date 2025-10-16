def calcular_media(numeros):
    with open(numeros, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]
        integers = []
        for i in lines:
            integer = int(i)
            integers.append(integer)
        average = sum(integers)/len(integers)
        print(f"A média dos números é: {average}")
calcular_media("numeros.txt")