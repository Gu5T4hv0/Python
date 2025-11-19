import pandas as pd

df = pd.read_json("clima.json")

media_temp = df["temperatura"].mean()
dias_chuva = (df["chuva"] > 0).sum()

print(media_temp)
print(dias_chuva)
