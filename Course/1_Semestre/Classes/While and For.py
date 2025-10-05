# for numero in range(3, 10, 2):
#     print(numero)

# nome = "Eduardo Mendes"

# for letra in nome:
#     print(letra)

# dias = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']

# for dia in dias:
#     print(dia)

# teste = "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"

# for palavra in teste.split(" "):
#     if len(palavra) >= 5:
#         print(palavra)


# numero = 1
# while numero <= 10:
#     print(numero)
#     numero += 1

numero = 1
while numero % 2 == 1:
    print(numero)
    numero = int(input("Digite um numero: "))

#precisa de alguma condição que o faça parar

#se eu ja sei que existe um limite de vezes use o for
#se eu não sei o limite de vezes use o while

#senha incorreta, enquanto não digitar certo use o while para repetir a msg
#

#for numero in range(3, 10, 2): {esse dois é o passo que ele vai ter, de dois em dois}
#for letra in nome: == {para cada casinha dentro da string imprima a casinha}