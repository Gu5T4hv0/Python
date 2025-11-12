import numpy as np
import matplotlib.pyplot as plt

random = np.random.randint(0,11,50)
plt.hist(random, bins=np.arange(0, 12) - 0.5, edgecolor='black')
plt.title("Distribuição de Notas da Turma")
plt.ylabel("Notas")
plt.xlabel("Número de Alunos")
plt.show()

print(random)