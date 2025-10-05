def forca(secreta: str, tentativas: list[str]) -> None:
    MAX_ERROS = 6
    erros = 0
    acertos = "_" * len(secreta)
    print(acertos)
    jaAcertou = False
    for letra in tentativas:
        posicoes = posicoes_da_letra(secreta, letra)
        if len(posicoes) > 0:
            acertos = substituir_letra(acertos, posicoes, letra)
            print(acertos)
            jaAcertou = acertou(acertos, secreta, erros, MAX_ERROS)
        else:
            erros += 1
        
        if jaAcertou or erros >= MAX_ERROS:
            break
        
    resultado = "ganhou" if jaAcertou else "perdeu"
    print(f"{resultado}, erros = {erros}")

def posicoes_da_letra(palavra: str, letra: str) -> list[int]:
    posicoes = []
    for i in range(len(palavra)):
        if palavra[i] == letra:
            posicoes.append(i)
    return posicoes

def pdl(palavra: str, letra: str) -> list[int]:
    return [i for i in range(len(palavra)) if letra == palavra[i]]

def substituir_letra(acertos: str, posicoes: list[int], letra: str) -> str:
    resultado = []
    for i in range(len(acertos)):        
        resultado.append(letra if i in posicoes else acertos[i])
    return "".join(resultado)

def sul(acertos: str, posicoes: list[int], letra: str) -> str:
    return "".join([letra if i in posicoes else acertos[i] for i in range(len(acertos))])

def acertou(acertos, secreta, erros, maximo):
    return acertos == secreta and erros < maximo