import pandas as pd

df = pd.read_json("filmes.json")
medias = df.groupby("filme")["nota"].mean()
print(medias)
