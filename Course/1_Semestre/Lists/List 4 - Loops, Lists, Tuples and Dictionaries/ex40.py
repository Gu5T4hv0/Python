# Given a tuple with names, display all names that begin with the letter "A".
names = ("Amélie", "Élodie", "Antoine","Adrien", "Julien")

a_names = []
for i in names:
    if i[0] == "A":
        a_names.append(i)

print(a_names)