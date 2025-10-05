def verificar_anagrama(palavra1, palavra2):
    letters = []
    for i in palavra1:
        lower = i.lower()
        letters.append(lower)

    letters2 = []
    for j in palavra2:
        lower2 = j.lower()
        letters2.append(lower2)

    if sorted(letters) == sorted(letters2):
        print("It is an anagrama!")
    else:
        print("It is not an anagrama!")


verificar_anagrama("Abacate", "cataeba")