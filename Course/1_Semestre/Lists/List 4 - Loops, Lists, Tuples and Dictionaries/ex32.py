# Make a program that reads 5 numbers and stores them in a tuple. Then display them in ascending order.
temp_list = []
for i in range(5):
    number = int(input("Type a number: "))
    temp_list.append(number)

numbers = tuple(temp_list)

increased = sorted(numbers)

print(increased)