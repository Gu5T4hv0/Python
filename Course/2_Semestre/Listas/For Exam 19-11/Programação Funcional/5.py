data = [1, 2, 3, 4, 5]
result = [x * x for x in [x for x in data if x % 2 == 0]]
print(result)