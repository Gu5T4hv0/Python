# def selection_sort(list) -> list:
#     values = []
#     for i in list:
#         values.append(i)

#     minor = min(values)
#     index = values.index(minor)
#     print(f"O menor valor é {minor} e o seu indice é {index}")


# selection_sort([1,2,3,4,5,6])

def selection_sort(lista: list) -> list:
    for i in range(len(lista)):
        indice_do_menor = i

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_do_menor]:
                indice_do_menor = j

        lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]

exemplo = [5,4,7,0,8,1,2,9,3,6]
print(exemplo)
selection_sort(exemplo)
print(exemplo)