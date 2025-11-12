import json
def indice_invertido(text, new_file):
    with open(text, "r", encoding="UTF-8") as file:
        words = {}
        for line_number, line in enumerate(file, start=1):
            liner = line.split()
            for i in liner:
                if i not in words:
                    words[i] = [line_number]
                else:
                    words[i].append(line_number)
        print(words)

    with open(new_file, "w", encoding="UTF-8") as filo:
        json.dump(words, filo, indent=4, ensure_ascii=False)

indice_invertido("large.txt", "json.json")