# Given a 3x3 matrix that represents the result of an old game, show a message with the current state of the game. Using capital letters X and O
def verificar_jogo(tabuleiro):
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] and tabuleiro[0][0] != 0:
        if tabuleiro[0][0] == 1:
            return "X ganhou"
        else:
            return "O ganhou"

    if tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] and tabuleiro[1][0] != 0:
        if tabuleiro[1][0] == 1:
            return "X ganhou"
        else:
            return "O ganhou"

    if tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][0] != 0:
        if tabuleiro[2][0] == 1:
            return "X ganhou"
        else:
            return "O ganhou"

    if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] and tabuleiro[0][0] != 0:
        if tabuleiro[0][0] == 1:
            return "X ganhou"
        else:
            return "O ganhou"

    if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] and tabuleiro[0][1] != 0:
        if tabuleiro[0][1] == 1:
            return "X ganhou"
        else:
            return "O ganhou"

    if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] and tabuleiro[0][2] != 0:
        if tabuleiro[0][2] == 1:
            return "X ganhou"
        else:
            return "O ganhou"

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != 0:
        if tabuleiro[0][0] == 1:
            return "X ganhou"
        else:
            return "O ganhou"

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != 0:
        if tabuleiro[0][2] == 1:
            return "X ganhou"
        else:
            return "O ganhou"

    for linha in tabuleiro:
        for elemento in linha:
            if elemento == 0:
                return "Jogo ainda não acabou"

    return "Jogo empatado"


jogo = [
    [0, 0, 1],
    [0, 1, 2],
    [2, 1, 0]
]

mensagem = verificar_jogo(jogo)
print(mensagem)
