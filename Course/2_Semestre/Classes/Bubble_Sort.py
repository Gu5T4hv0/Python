def bubble_sort(lista:list) -> list:
    passou = 0
    trocou = 0
    for j in range(len(lista) -1):
        jaOrdenado = True
        for i in range(len(lista) -1 -j):
            passou += 1
            #print(f"{passou}\r", end="")
            atual = lista[i]
            proximo = lista[i + 1]

            if atual > proximo:
                jaOrdenado = False
                trocou += 1
                lista[i], lista[i + 1] = proximo, atual
                print(lista)

        if jaOrdenado:
            break

    print(f"Passou: {passou}. Trocou: {trocou}")
    return lista

exemplo = [3,0,1,8,7,2,5,4,6,9]
print(exemplo)
bubble_sort(exemplo)
print(exemplo)
bubble_sort(exemplo)
exemplo.sort(reverse=True)
bubble_sort(exemplo)

# import random
# novo = []
# for _ in range(100_000):
#     novo.append(random.radint(10, 100000))

# bubble_sort(novo)