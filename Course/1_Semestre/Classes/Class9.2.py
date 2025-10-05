num = 16500
keys = {
    "a" : 6,
    "b" : 1,
    "d" : 7,
    "e" : 4,
    "i" : 3,
    "l" : 2,
    "m" : 9,
    "n" : 8,
    "o" : 0,
    "t" : 5,
}

word = ""
for digito in str(num):
    for key in keys:
        if keys[key] == int(digito):
    letra = keys.values
    if letra in keys:
        word += keys[letra]

return word

errado