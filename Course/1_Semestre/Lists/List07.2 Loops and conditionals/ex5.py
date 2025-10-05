# Given an array of integers, find the element that appears most often in the array. If there are several elements with the same maximum frequency, return any of them.
matrix = [[2, 5, 2, 7],
        [5, 2, 7, 3],
        [9, 2, 5, 7],
        [2, 5, 7, 9]]

dictio = {}
for line in matrix:
    for number in line:
        if number in dictio:
            dictio[number] += 1
        else:
            dictio[number] = 1
print(dictio)

most_commun = max(dictio, key=dictio.get)
print(most_commun)