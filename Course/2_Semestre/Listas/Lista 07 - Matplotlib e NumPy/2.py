import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 11)
height = np.array([5, 7, 9, 12, 14, 15, 17, 19, 21, 23])

m, b = np.polyfit(days, height, 1)
trend = m * days + b

plt.scatter(days, height, label="Measured Height")
plt.plot(days, trend, color='red', label="Trend Line (Linear Fit)")
plt.xlabel("Days")
plt.ylabel("Height (cm)")
plt.title("Plant Growth Over 10 Days")
plt.legend()
plt.show()
