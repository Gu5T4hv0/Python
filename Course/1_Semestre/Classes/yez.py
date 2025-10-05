# number = int(input("Type a number and i will give you the times table: "))

# for i in range(1, 11):
#     print(f"{number} * {i} = {number * i}")


# number = -1
# numbers = []
# while number != 0:
#     number = int(input("Type a number: "))
#     if number != 0:
#         numbers.append(number)

# summer = sum(numbers)
# print(f"The sum of the typed numbers is: {summer}")

# dictionaire = {
#     "name": f"{name}",
#     "age": f"{age}",
#     "favorite_foods": ()
# }

# nome = "Eduardo Mendes"

# nome.split(" ")
# nome[0]
# len(nome[0])

# print(nome)

def inverter_lista(lista):
    lista_invertida = lista[::-1]
    print(lista_invertida)
    return lista_invertida

inverter_lista([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]