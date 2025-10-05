# Make a program that counts the frequency of letters in a word using a dictionary.
word = input("Type a word: ")
letter_count = {}

for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print("Letter frequency:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")