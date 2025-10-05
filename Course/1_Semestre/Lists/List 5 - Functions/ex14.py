# Based on the previous question, implement a function that decrypts the string.
def descriptografia(criptografado):
    partes = criptografado.split('#')
    tamanho = 0
    for p in partes:
        letras_pos = p.split('=')
        posicoes = letras_pos[1].split('&')
        for pos in posicoes:
            if int(pos) > tamanho:
                tamanho = int(pos)
    tamanho += 1
    resultado = [''] * tamanho

    for p in partes:
        letra, posicoes_str = p.split('=')
        posicoes = posicoes_str.split('&')
        for pos in posicoes:
            resultado[int(pos)] = letra

    return ''.join(resultado)

codigo = 'A=0# =1&6#c=2&7#a=3&5&8#s=4#i=9#u=10'
print(descriptografia(codigo))