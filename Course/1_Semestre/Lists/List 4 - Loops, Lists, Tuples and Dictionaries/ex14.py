# Count how many numbers typed by the user are positive. The program should stop when a negative number is typed.
numbers = []
while True:
    number = int(input("Type a number: "))
    if number < 0:
        break
    numbers.append(number)
        
lenght = len(numbers)

print(lenght)