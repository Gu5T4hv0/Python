# Crie uma função que receba uma temperatura em Celsius e a converta para Fahrenheit:
def celsius_to_fahrenheit(c):
    calc = 9/5
    f = c*calc + 32
    print(f"{f}°F")
    return f
celsius_to_fahrenheit(40)