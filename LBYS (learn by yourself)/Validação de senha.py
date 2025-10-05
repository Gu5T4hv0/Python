senha_correta = "python123"
senha = -1

while senha != senha_correta:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Senha correta")
    else:
        print("Senha incorreta")