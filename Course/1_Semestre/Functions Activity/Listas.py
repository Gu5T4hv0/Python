# def criar_lista(): → Retorna uma lista com números de 1 a 20.
def criar_lista():
    lista = []
    for i in range(1, 21):
        lista.append(i)
    return lista
# def adicionar_elemento(lista, elemento): → Adiciona um elemento ao final da lista.
def adicionar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

# def remover_elemento(lista, elemento): → Remove um elemento da lista, se existir.
def remover_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista

# def contar_ocorrencias(lista, elemento): → Conta quantas vezes um elemento aparece.
def contar_ocorrencias(lista, elemento):
    counter = lista.count(elemento)
    return counter

# def contem_elemento(lista, elemento): → Retorna True se o elemento estiver na lista.
def contem_elemento(lista, elemento):
    if elemento in lista:
        return True
    else:
        return False

# def inverter_lista(lista): → Retorna a lista invertida.
def inverter_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

# def ordenar_crescente(lista): → Retorna a lista ordenada em ordem crescente.
def ordenar_crescente(lista):
    lista.sort()
    return lista

# def ordenar_decrescente(lista): → Retorna a lista ordenada em ordem decrescente.
def ordenar_decrescente(lista):
    lista.sort(reverse=True)
    print(lista)
    return lista

# def somar_lista(lista): → Retorna a soma de todos os elementos.
def somar_lista(lista):
    summing = sum(lista)
    return summing

# def media_lista(lista): → Retorna a média dos valores.
def media_lista(lista):
    media_lista = sum(lista)/len(lista)
    return round(media_lista, 1)

# def filtrar_pares(lista): → Retorna apenas os elementos pares.
def filtrar_pares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares
        
# def quadrados(lista): → Retorna uma nova lista com os quadrados dos elementos.
def quadrados(lista):
    NQuadrados = []
    for i in lista:
        calc = i * i
        NQuadrados.append(calc)
    return NQuadrados

# def copiar_lista(lista): → Retorna uma cópia da lista.
def copiar_lista(lista):
    copiar = lista.copy()
    return copiar

# def concatenar_listas(lista1, lista2): → Retorna a junção das duas listas.
def concatenar_listas(lista1, lista2):
    junção = lista1 + lista2
    return junção

# def limpar_lista(lista): → Esvazia a lista (in-place).
def limpar_lista(lista):
    lista.clear()
    return lista