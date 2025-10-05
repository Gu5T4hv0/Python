def descriptografar(message, code):
    binario = format(code, f'0{len(message)}b')
    resultado = ""
    for i in range(len(message)):
        if binario[i] == '1':
            resultado += message[i]
    return resultado

mensagem = "abcdef"
codigo = 5

print(descriptografar(mensagem, codigo))