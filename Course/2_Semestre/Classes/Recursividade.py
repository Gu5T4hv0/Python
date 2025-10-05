def somado(lista: list) -> int:
    res = 0
    for i in lista:
        res += i
    return res

a = [5, 10, 15, 20, 25]
r = somado(a)
print(r)

def somar(jr:list, i:int) -> int:
    if i < len(jr):
        return jr[i] + somar(jr, i+1)
    else:
        return 0

a = [5, 10, 15, 20, 25]
r = somar(a, 0)