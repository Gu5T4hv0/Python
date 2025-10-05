# Write a code that asks for names until the word "end" is typed, and then displays all of the typed names.
names = []
name = ""
while name.lower() != "end":
    name = input("Type a name: ")
    names.append(name)

names.pop()
for name in names:
    print(name)