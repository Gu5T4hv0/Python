nome_completo = input("Digite seu nome completo: ")
idade = input("Digite sua idade: ")
profissão = input("Digite sua profissão?: ")

concatenar = str(nome_completo[ :3]) + idade
maiuscula = profissão.upper()
nome_separado = nome_completo.split()
primeiro_nome = nome_separado[0].capitalize()
ano_de_nascimento = 2025 - int(idade)
print(f"Olá, {primeiro_nome}! Seu nome de usuário é \"{concatenar}\". \nVocê tem {idade} anos, trabalha como {maiuscula} e nasceu em {ano_de_nascimento}.")