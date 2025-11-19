import pandas as pd

df = pd.read_json("estoque.json")
valor_total = (df["quantidade"] * df["preço"]).sum()
print(valor_total)