word = str(input("Type a word: "))

word_list = word.split()
new_list = []
for i in word_list[::-1]:
    new_list.append(i)

result = " ".join(new_list)
print(result)