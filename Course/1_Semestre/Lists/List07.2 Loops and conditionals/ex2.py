# Make an algorithm that receives a binary and converts the value into an integer.
binary = 10010
str_binary = str(binary)

reversed_digits = []
for digit in str_binary[::-1]:
    reversed_digits.append(digit)

integrado = []
for digit in reversed_digits:
    integer_digit = int(digit)
    integrado.append(integer_digit)

positions = []
for i in range(len(str_binary)):
    positions.append(i)

calculated = []
for pos in positions:
    power_of_two = 2 ** pos
    calculated.append(power_of_two)

calculated_products = []
for digit, power in zip(integrado, calculated):
    result = digit * power
    calculated_products.append(result)

summing = sum(calculated_products)

print(summing)
