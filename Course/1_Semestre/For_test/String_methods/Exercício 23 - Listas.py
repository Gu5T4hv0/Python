lista = [1, 3, 6, 2, 1, 1]

new_list = []
for i in lista:
    if i not in new_list:
        new_list.append(i)
print(new_list)