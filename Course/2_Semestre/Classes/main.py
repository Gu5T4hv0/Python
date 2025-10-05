# import lib.calculadora
# import lib.calculadora as c

# x = 1
# y = 2
# resultado = lib.calculadora.somar(x,y) or resultado = c.somar(x,y)

# print(resultado)

# from lib.calculadora import somar

# x = 1
# y = 2
# resultado = somar(x,y)

# print(resultado)


from lib.calculadora import *

x = 1
y = 2
mais = somar(x,y)
menos = subtrair(x,y)
multiplo = multiplicar(x,y)
dividido = dividir(x,y)

print(mais, menos, multiplo, dividido)