# Allow the user to search for a key in the dictionary and display the corresponding value.
french = {
    "dog": "chien",
    "cat": "chat",
    "rat": "souris",
    "horse": "cheval"
}

animal = input("Type an animal: ")

if animal in french:
    print(f"This {animal} in french is {french[animal]}")