phrase = "a mancha verde é o poder"

spliter = phrase.split()
words = []
for i in spliter:
    if len(i) >= 5:
        words.append("#" + i.capitalize())

print(" ".join(words))