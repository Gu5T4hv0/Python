import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")
df["Faturamento"] = df["Quantidade"] * df["Preço"]

totais = df.groupby("Produto")["Faturamento"].sum()

plt.bar(totais.index, totais.values)
plt.xlabel("Produto")
plt.ylabel("Faturamento")
plt.title("Faturamento por Produto")
plt.show()
