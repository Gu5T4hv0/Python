# Create a function called "vowel counter" that takes a string as argument and returns the number of vowels in the string.
def vowel_counter(string):
    vowels = "aeiou"
    counter = 0
    for i in string:
        lower = i.lower()
        if lower in vowels:
            counter += 1
    return counter

vowel_counter("Engineering")