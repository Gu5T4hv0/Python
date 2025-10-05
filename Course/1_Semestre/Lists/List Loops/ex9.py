# Make an algorithm that determines whether or not there are double characters in a string (including whitespace characters). For example aa, !! or (space and space). Show True if the string contains double characters and False if not. The test should be case-insensitive; for example, both aa and aA show True.
sentence = "aAb cC !!"
dictio = {}

for i in sentence:
    letter = i.lower()
    if letter in dictio:
        dictio[letter] += 1
    else:
        dictio[letter] = 1

counter = 0
for value in dictio.values():
    if value > 1:
        counter += 1
    else:
        counter = 0

if counter != 0:
    print(True)
else:
    print(False)
