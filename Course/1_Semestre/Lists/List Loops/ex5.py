phrase = "How can mirrors be real if our eyes aren't real"

spliter = phrase.split()
newphrase = []
for i in spliter:
    capitalizor = i.capitalize()
    newphrase.append(capitalizor)
    
joiner = " ".join(newphrase)
print(joiner)