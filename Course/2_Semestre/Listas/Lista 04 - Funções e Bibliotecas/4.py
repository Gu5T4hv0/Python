import secrets
import string

def gerar_senha(tam, maiusculas=True, digitos=True, simbolos=True):
    letras = string.ascii_lowercase
    if maiusculas == True:
        maiusculas = string.ascii_uppercase
    else:
        maiusculas = ""

    if digitos == True:
        digitos = string.digits
    else:
        digitos = ""

    if simbolos == True:
        simbolos = string.punctuation
    else:
        simbolos = ""
    
    alphabet = letras + maiusculas + digitos + simbolos

    if not alphabet:
        raise ValueError("Você deve escolher pelo menos um conjunto de caracteres!")
    
    password = ""
    for i in range(tam):
        random_char = secrets.choice(alphabet)
        password = password + random_char

    print(password)
    return password
gerar_senha(10, True, True, False)