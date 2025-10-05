import random
while True:
    usuario = input("Escolha entre pedra papel de tesoura: ")
    valor_aleatorio = random

    if valor_aleatorio == 1:
        computador = ('pedra')
    elif valor_aleatorio == 2:
        computador = ('papel')
    else:
        computador = ('tesoura')

    voce_ganhou = (usuario == ('pedra'), computador == ('tesoura')) \
                    (usuario == ('papel'), computador == ('pedra')) \
                    (usuario == ('tesoura'), computador == ('papel'))
    
    if voce_ganhou:
        print('Você ganhou!')
    elif usuario == computador:
        print('Empate')
    else:
        print('Você perdeu!')

    print('Usuário: ', usuario, '\nComputador', computador)