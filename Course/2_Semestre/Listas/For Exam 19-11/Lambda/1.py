people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 45},
    {'name': 'David', 'age': 19},
    {'name': 'Eve', 'age': 22}
]

names = list(map(lambda pessoa: pessoa['name'].upper(), filter(lambda person: person['age'] >= 18, people)))
print(names)