# Erstellen Sie eine Funktion namens Quadrat, die zwei Parameter erhält, einen für die Basis und einen anderen für die Höhe zeigen den Rand eines Quadrats durch Sternchen gemacht.
def quadrado(base, altura):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            print('* ' * base)
        else:
            meio = '  ' * (base - 2)
            print('* ' + meio + '*')

quadrado(5, 3)