import pandas as pd

reader = pd.read_csv("jogos.txt", sep=",", names=["Jogador", "Pontuação"])

sorter = reader.sort_values("Pontuação", ascending=False)
print(f"Ranking\n{sorter}\n")

loc = sorter.iloc[0]
print(f"O Ganhador(a) é \n{loc}")