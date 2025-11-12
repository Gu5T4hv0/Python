import matplotlib.pyplot as plt
import numpy as np

y = [30, 32, 31, 29, 28, 33, 34]

media = np.mean(y)
minima = np.min(y)
maxima = np.max(y)
print(f"média = {media}, mínima = {minima}, máxima = {maxima}")

plt.plot(y, color = "red")
plt.title("Clima")
plt.xlabel("Days of the week")
plt.ylabel("Clima of the week")
plt.show()