# Create a function called "verify_anagrama" that takes two strings as arguments and returns True if the strings are anagramas (i.e., they have the same letters regardless of order), and False otherwise.
def verify_anagrama(a, b):
    letters = "abcdefghijklmnopqrstuvwxyz"
    countera = []
    for i in a:
        lower = i.lower()
        if lower in letters:
            countera.append(lower)
    counterb = []
    for i in b:
        lower = i.lower()
        if lower in letters:
            counterb.append(lower)
    if sorted(countera) == sorted(counterb):
        print(True)
        return True
    else:
        print(False)
        return False

verify_anagrama("Computer", "Pmteruoc")