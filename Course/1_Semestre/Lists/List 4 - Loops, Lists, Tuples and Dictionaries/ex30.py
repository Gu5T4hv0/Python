# Make a program that reads a list of numbers and displays only those between 10 and 50.
random_numbers = [37, 82, 14, 59, 3, 91, 26, 68, 45, 77]

selected_numbers = []
for i in random_numbers:
    if i >= 10 and i <= 50:
        selected_numbers.append(i)

selected_numbers.sort()
print(selected_numbers)