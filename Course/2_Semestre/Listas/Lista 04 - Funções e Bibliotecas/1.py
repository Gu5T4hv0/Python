import statistics

vendas = [10,12,13,11,60,12,14,13]

media = statistics.mean(vendas)
print(f"Média: {media}")

mediana = statistics.median(vendas)
print(f"Mediana: {mediana}")

moda = statistics.mode(vendas)
print(f"Moda: {moda}")

desvio = statistics.stdev(vendas)
print(f"Desvio: {desvio}")

outliers = []
limite = 2

for x in vendas:
    z_score = (x - media)/ desvio
    if abs(z_score) > limite:
        outliers.append(x)

print(outliers)