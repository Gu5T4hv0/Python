import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 31)
prices = np.random.randint(1, 11, 30)
print(prices)
colors = []
size = []

for i in range(len(prices)):
    if prices[i] > 8:
        colors.append("red")
        size.append(50)
    else:
        colors.append('blue')
        size.append(0.1)

plt.scatter(days, prices, c=colors, s=size)
plt.plot(days, prices)
plt.show()