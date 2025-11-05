import csv
def relatorio_de_vendas(origem, destino):
    by_product = {}
    with open(origem, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for i in reader:
            product = i[1]
            qtd = int(i[2])
            price = float(i[3])
            count = qtd * price
            date = i[0].split("-")
            date2 = "-".join([date[0], date[1]])
            if product not in by_product:
                by_product[product] = 0
            by_product[product] += count
            if date2 not in by_product:
                by_product[date2] = 0
            by_product[date2] += count

        names = {}
        dates = {}
        for key, value in by_product.items():
            if any(char.isdigit() for char in key):
                dates[key] = value
            else:
                names[key] = value
        new_by_product = {**names, **dates}
        total = 0
        for i,j in dates.items():
            total += j

    with open(destino, "w", encoding="utf-8") as file:
        file.write(f"total = {total}\n")
        for name, dates in new_by_product.items():
            file.write(f"{name} = {dates}\n")
        
relatorio_de_vendas("vendas.csv", "relatorio.txt")