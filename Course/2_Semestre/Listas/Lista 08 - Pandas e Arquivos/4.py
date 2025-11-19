import pandas as pd

df = pd.read_csv("notas.csv")
df["Média"] = (df["Prova1"] + df["Prova2"]) / 2
aprovados = df[df["Média"] >= 6]
print(aprovados)
