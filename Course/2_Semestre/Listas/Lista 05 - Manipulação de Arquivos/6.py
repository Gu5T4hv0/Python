import csv
def controle_de_presenca(arquivo):
    presences = {}
    with open(arquivo, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for i in reader:
            name = i[0]
            presence = int(i[2])
            if name not in presences:
                presences[name] = []
            presences[name].append(presence)
            
        for key, value in presences.items():
            percentage = (sum(value)/len(value))*100
            print(f"{key}: {percentage:.2f}% presença (faltas = {sum(value)}/{len(value)})")

controle_de_presenca("presenca.csv")