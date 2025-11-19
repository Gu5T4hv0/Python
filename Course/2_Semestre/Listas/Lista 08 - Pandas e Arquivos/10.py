import pandas as pd

df = pd.read_csv("onibus.txt")

totais = df.groupby("linha")["passageiros"].sum()
mais_movimentada = totais.idxmax()

print(totais)
print(mais_movimentada)
