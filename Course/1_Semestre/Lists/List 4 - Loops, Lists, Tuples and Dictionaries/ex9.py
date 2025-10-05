# Create a guessing game: the computer chooses a number from 1 to 100 and the user tries to guess.
import random
numbers = []
for i in range(1, 101):
    numbers.append(i)

computer = random.choice(numbers)

user = int(input("Guess what number the computer had chosen: "))

if user == computer:
    print(f"Congratulations the computer choose {computer} and you {user}. It matches!")
else:
    print(f"What a shame! the computer choose {computer} and you {user}, Try again!")