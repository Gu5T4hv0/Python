# Read a tuple with 5 numbers and display the number of even numbers.
numbers = (1, 2, 3, 4, 5)

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print(f"The quantity of even numbers in the list is {count}")