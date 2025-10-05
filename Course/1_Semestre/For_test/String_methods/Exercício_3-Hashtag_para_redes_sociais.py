entry = "a mancha verde é o poder"

spliter = entry.split()

words = []
for word in spliter:
    capitalizor = word.capitalize()
    if len(capitalizor) >= 5:
        words.append(capitalizor)

oficial_words = []
for word2 in words:
    oficial_words.append("#" + word2)

joiner = " ".join(oficial_words)
print(joiner)