import csv
def frequencia_de_palavras(texto, stop, top):
    with open(stop, "r", encoding="utf-8") as file:
        reader1 = [word.lower() for word in file.read().split()]
    with open(texto, "r", encoding="utf-8") as file:
        reader2 = file.read().split()
        new_txt = []
        for word in reader2:
            word = word.lower()
            word = ''.join(char for char in word if char.isalnum() or char.isspace())
            if word and word not in reader1:
                new_txt.append(word)
        count = {}
        for wrd in new_txt:
            if wrd in count:
                count[wrd] += 1
            else:
                count[wrd] = 1
        
        pairs = count.items()
        ordered = sorted(pairs, key=lambda item: item[1], reverse=True)
        ordered_dict = dict(ordered)

    with open(top, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["nome", "contador"])
        for nome, contador in ordered_dict.items(): writer.writerow([nome, contador])

frequencia_de_palavras("texto.txt", "stopwords.txt", "top_20.csv")