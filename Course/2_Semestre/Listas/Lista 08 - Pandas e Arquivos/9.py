import pandas as pd

df = pd.read_csv("clientes.csv")
medias = df.groupby("Cidade")["Idade"].mean()
print(medias)