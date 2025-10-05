def mostrar_tipos_dados(int, float, str):
    print(f"{int} = integer, {float} = float, {str} = string")
mostrar_tipos_dados(3, 3.5, "three")

def mostrar_parte_inteira():
    decimal = float(input("Give me a decimal number:"))
    print(f"The integer part of this number is {decimal:.0f}")
mostrar_parte_inteira()

def converter_string_para_inteiro():
    string = str(input("Type a number"))
    integer = int(string)
    summing = integer + 2
    print(f"The sum of your number by two is {summing}")
converter_string_para_inteiro()

def mostrar_tipo_booleano(boolean):
    print(type(boolean))
mostrar_tipo_booleano(True)