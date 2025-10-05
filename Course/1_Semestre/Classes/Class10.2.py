senha = 'unasp1234'
  
if len(senha) < 8:
    print("Senha Inválida")
else:
    senha = senha.lower()
    senha = senha.replace("a", "!")\
        .replace("e", "@")\
        .replace("i", "#")\
        .replace("o", "$")\
        .replace("u", "%")

    print(senha)