from functools import reduce
numbers = [2, 3, 4]

product = (reduce(lambda i,j: i*j, numbers))

print(product)