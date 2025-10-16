from Funções \
import somar, palindromo, contagem, soma_digitos, calcular_descontos

caixas = [3,5,2]
total = somar(caixas, 0)
print(f"Total: {total}")

print(palindromo("radar"))
print(palindromo("arara"))
print(palindromo("abcddcba"))
print(palindromo("chocolate"))

print(contagem(5), "\nDecolar!")

print(soma_digitos(987))

print(calcular_descontos([100, 200, 300], 1))