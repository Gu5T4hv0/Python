idade = int(input("Digite sua idade: "))
genero = input("Qual é o seu gênero de filme favorito?: ")

if idade < 12:
    print(f"Você tem {idade} e gosta de {genero}.\n Recomendamos: Filmes infantis!")
elif idade < 17:
    print(f"Você tem {idade} e gosta de {genero}.\n Recomendamos: Filmes de aventura ou comédia!")
else:
    print(f"Você tem {idade} e gosta de {genero}.\n Recomendamos: Qualquer outro tipo de filme!")