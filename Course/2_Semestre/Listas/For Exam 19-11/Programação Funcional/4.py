from functools import reduce
data = [1, 2, 3, 4, 5, 6]

filtered_numbers = list(filter(lambda i: i % 2 != 0, data))
squared_numbers = list(map(lambda j: j*j, filtered_numbers))
aggregated_numbers = reduce(lambda k, l: k + l, squared_numbers)

print(aggregated_numbers)

# another way
from functools import reduce
data = [1, 2, 3, 4, 5, 6]

# 1. Filter the odd numbers inside the map function's iterable slot.
# 2. Map squares them.
# 3. Reduce sums the final result.
result = reduce(lambda k, l: k + l, map(lambda j: j*j, filter(lambda i: i % 2 != 0, data)))

print(result) # Output: 35