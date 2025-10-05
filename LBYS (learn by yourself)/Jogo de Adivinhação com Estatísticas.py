user = input("Hello! What’s your name? ")
computer = 42
guesses = []
guess = None
tries = 0

while guess != computer:
    guess = int(input(f"Ok {user}, try to guess the number I’m thinking between 1 and 100. "))
    guesses.append(guess)
    tries += 1

    if guess > computer:
        print("Too high")
    elif guess < computer:
        print("Too low")



print(f"\nCongratulations, {user}! You guessed the number in {tries} tries.")
print("\nYour guesses were:")
for i, g in enumerate(guesses, 1):
    print(f"{i}: {g}")