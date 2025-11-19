import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**2 - 2*x + 1
print(y)
plt.plot(x,y)
plt.title("Projeção de Lucros")
plt.xlabel("Tempo")
plt.ylabel("Lucro")
plt.show()