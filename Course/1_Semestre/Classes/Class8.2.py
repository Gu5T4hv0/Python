# Growth of a Population
p0 = 1000
percent = 2
aug = 50
p = 1200

contador = 0

while p0 < p:
    p0 += int((p0 * (percent/100)) + aug)
    contador += 1 #conta quantos loops fez

print(contador)