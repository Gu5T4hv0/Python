import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y1 = np.array([20, 27, 18, 30, 35])
y2 = np.array([40, 36, 18, 21, 15])
print(x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("Tempo")
plt.ylabel("Temperatura")
plt.title("Séries temporais")
plt.show()