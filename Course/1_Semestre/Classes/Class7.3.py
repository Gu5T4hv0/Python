nota1 = float(input('digite a nota 1:'))
nota2 = float(input('digite a nota 2:'))
nota3 = float(input('digite a nota 3:'))

notas = []
notas.append(nota1)
notas.append(nota2)
notas.append(nota3)

media = sum(notas)/len(notas)

if media >= 6:
    print('aprovado')
else:
    print('reprovado')