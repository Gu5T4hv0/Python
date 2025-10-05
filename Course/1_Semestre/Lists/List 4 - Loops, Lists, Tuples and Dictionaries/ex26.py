# Receive 2 lists of 5 elements each and create a third with the sum of the elements of the same position.
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 5, 4, 3, 2]

sum = []
for a, b in zip(list_1, list_2):
    sum.append(a + b)

print(sum)