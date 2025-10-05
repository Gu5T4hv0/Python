import random
computer = random.randint(1, 100)

user = int(input("Guess the number the comupter choose: "))

while user != computer:
    if user > computer:
        print("A little lower")
    elif user < computer:
        print("A little higher")

    user = int(input(f"The computer choose {computer}. Try again:"))

print("Congrats, you guessed it!")