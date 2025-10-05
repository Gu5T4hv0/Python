nome = input("Digite seu nome: ").strip()

if " " in nome:
    print("Nome inválido: não pode conter espaços.")
elif not nome.isalpha():
    print("Nome inválido: use apenas letras.")
elif not (len(nome) > 4 and len(nome) < 16):
    print("Nome inválido: deve ter entre 5 e 15 caracteres.")
else:
    print(f"Nome válido! Bem-vinda, {nome.capitalize()}!")

