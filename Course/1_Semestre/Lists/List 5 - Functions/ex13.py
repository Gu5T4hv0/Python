# Implement a function that receives a phrase and turn it into an encrypted string. The encrypted string must contain each character present in the sentence, followed by its positions in the original string. Each character must be followed by the = symbol and their positions separated by &. Different characters must be separated by #. The sentence should only contain uppercase or lowercase letters and numbers and spaces.
def criptografia(texto):
    dicio = {}
    for i in range(len(texto)):
        letra = texto[i]
        if letra in dicio:
            dicio[letra].append(str(i))
        else:
            dicio[letra] = [str(i)]

    lista_cripto = []
    for key in dicio:
        cripto_parcial = '&'.join(dicio[key])
        lista_cripto.append(f"{key}={cripto_parcial}")
    print('#'.join(lista_cripto))
    return '#'.join(lista_cripto)

criptografia('A casa caiu')