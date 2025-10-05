# Ask the user for 5 letters and store in a tuple. Then display the typed vowels.
temp_letters = []
for i in range(5):
    letter = input("Type a letter: ")
    letter.lower()
    if letter in ('a', 'e', 'i', 'o', 'u'):
        temp_letters.append(letter)

letters = tuple(temp_letters)

print(f"The vowels that you typed are {letters}")