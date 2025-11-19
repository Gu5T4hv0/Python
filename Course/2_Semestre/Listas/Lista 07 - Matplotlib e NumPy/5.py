import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(1, 100, 60)
y = np.random.randint(1, 100, 60)

plt.plot(x,y)
plt.title("Runner position")
plt.xlabel("Horizontal")
plt.ylabel("Vertical")
plt.show()