a = "Duda"
b = a.startswith("F")
print(b)

l4 = [10, "Pedro"]
print(l4[0]*2)
print(l4[1].upper())

d = {
    "mes":11,
    "dia":25,
    "ano":83,
    "3":8
}

print(d["dia"])

familia = {
    "pai": "almir",
    "mae": "bel",
    "filhos": ["arthur, emilly"]
}
print(familia["filhos"])
print(familia)
familia["filhos"].append("arthur2")
print(familia)

x = [5, 10, 15, 20, 25, 30, 35, 40, 45]
print(x[1:5])
print(x[2: ])
print(x[ :5])
print(x[ : ])#msm coisa de print(x)
print(x[-4])
print(x[1:8:2])#o terceiro numero é de dois em dois(em quantos passos)
# 1 é inclusivo e 5 é exclusivo(não entra) o primeiro é inclusivo e o ultimo é exclusivo


dias = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]

for i in dias:
    if "a" in i:
        print(f"no {i} tem a letra 'a'")

for i in range(len(dias)):
    if "a" in dias[i]:
        print(dias[i])

for indice in range(7):
    print("O mundial do palmeiras é igual a zero")

for indice in range(7):
    print(indice)
for indice in range(2, 7):
    print(indice)
for indice in range(1, 10, 2):
    print(indice)

indice = 0
while indice < 7:
    print(dias[indice])
    indice += 1