# Request 10 numbers from the user and display the arithmetic mean.
sum = []
for i in range(10):
    inputer = int(input("Digite um número: "))
    sum.append(inputer)

media = sum(sum) / len(sum)
print(media)