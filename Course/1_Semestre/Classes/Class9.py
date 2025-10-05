#Turn any word into a beef taco
word = 'ogl'
ingredientes = {
    'a': 'beef',
    'e': 'beef',
    'i': 'beef',
    'o': 'beef',
    'u': 'beef',
    't' : 'tomato',
    'l' : 'lettuce',
    'c' : 'cheese',
    'g' : 'guacamole',
    's' : 'salsa',
}

taco = ['shell']

for letra in word:
    if letra in ingredientes:
        taco.append(ingredientes[letra])

taco.append('shell')
print(taco)