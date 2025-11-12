import pandas as pd

df = pd.read_csv("presenca.csv")

faltas = df[df["Presente"] == "Não"].groupby("Aluno").size()

print(faltas)