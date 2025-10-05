from collections import Counter
frase = "Bom dia, bom humor, bom trabalho!"

ponctuations = ".!?:,;—/-"
noPonctuations = []
lowercase = []
for i in frase:
    if i not in ponctuations:
        noPonctuations.append(i)

for minor in noPonctuations:
    small = minor.lower()
    lowercase.append(small)

whole = "".join(lowercase)
spliter = whole.split()

word_counts = Counter(spliter)

print(word_counts)