import pandas as pd

df = pd.read_csv("gastos.csv")
totais = df.groupby("Categoria")["Valor"].sum()
mais_cara = totais.idxmax()
print(totais)
print("Mais cara:", mais_cara)