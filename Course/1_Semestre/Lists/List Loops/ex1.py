# Given an array of integers, show the number that appears an odd number of times. There will always be only one integer that appears an odd number of times.
array = [1,2,2,3,3,3,4,3,3,3,2,2,1]
dictio = {}
for i in array:
    if i in dictio:
        dictio[i] += 1
    else:
        dictio[i] = 1

for key, value in dictio.items():
    if value % 2 != 0:
        print(key)