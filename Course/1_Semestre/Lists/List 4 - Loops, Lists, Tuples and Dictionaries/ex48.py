# Remove an item from a dictionary based on a key entered by the user.
translate = {
    "banana": "banane",
    "strawberry": "fraises",
    "lemon": "citron",
    "pear": "pêche"
}

print(translate)
fruit = input("Remove a fruit in english: ")

if fruit in translate:
    translate.pop(fruit)
    print(f"The {fruit} is no longer in {translate}")
else:
    print("Fruit not found in dictionary")