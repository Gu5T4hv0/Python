# Given a dictionary with the name and age of several people, display only those over 18.
ages = {
    "Catarina": 19,
    "João": 10,
    "Alberto": 5,
    "Antônio": 32
}

print("The adults are:")
for key, value in ages.items():
    if value >= 18:
        print(f"{key} with {value} years old")