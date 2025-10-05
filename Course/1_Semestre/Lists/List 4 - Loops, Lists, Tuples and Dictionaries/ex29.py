# Check if a number is present in a list.
number = int(input("Type a number that you think is in the list: "))
list = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

if number in list:
    print(f"The number {number} is in the list and occupies the place {list.index(number)}")
else:
    print("What a shame, your number is not in the list!")