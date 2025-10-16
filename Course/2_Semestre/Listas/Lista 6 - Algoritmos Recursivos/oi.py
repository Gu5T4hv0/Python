def somar(lista):
    if len(lista) == 0:          # caso base
        return 0
    else:
        print(lista[0] + somar(lista[1:]))
        return lista[0] + somar(lista[1:])
    
somar([1,2,3])