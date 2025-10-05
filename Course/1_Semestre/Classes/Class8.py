# Square Every Digit
numero = 9119

texto = ""
while numero > 0:
    digito = numero % 10
    potencia = digito ** 2
    texto = str(potencia) + texto
    numero //= 10

resultado = int(texto) if texto != "" else 0
print(texto)