import random
while True:
    usuario = input('pedra, papel e tesoura?').lower()
    valor_aleatorio = random.randint(1,3)

    if valor_aleatorio == 1:
        computador = 'pedra'
    elif valor_aleatorio == 2:
        computador = 'papel'
    else:
        computador = 'tesoura'

    voce_ganhou = (usuario == 'pedra' and computador == 'tesoura') \
            or (usuario == 'papel' and computador == 'pedra') \
            or (usuario == 'tesoura' and computador == 'papel')

    if voce_ganhou:
        print("Você Ganhou!")
    elif usuario == computador:
        print("Empate")
    else:
        print("Você Perdeu!")

    print("Usuário = ", usuario,"\nComputador = ", computador)