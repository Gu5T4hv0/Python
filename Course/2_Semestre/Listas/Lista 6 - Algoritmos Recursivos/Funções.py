def somar(lista: list[int], i:int) -> int:
    if i < len(lista):
        return lista[i] + somar(lista, i + 1)
    else:
        return 0
    
def palindromo(palavra:str) -> bool:
    if len(palavra) > 1:
        if palavra[0] == palavra[-1]:
            return palindromo(palavra[1:-1])
        else:
            return False
    else:
        return True

def contagem(numero:int):
    if numero > 0:
        print(numero)
        return contagem(numero - 1)
    else:
        return 0

def soma_digitos(numero:int):
    if numero != 0:
        ultimo = numero % 10
        resto = numero // 10
        return ultimo + soma_digitos(resto)
    else:
        return 0

def calcular_descontos(lista:list, discount):
    if len(lista) == 0:
        return 0
    else:
        return lista[0]*(discount - 0.1) + calcular_descontos(lista[1:], discount - 0.1)