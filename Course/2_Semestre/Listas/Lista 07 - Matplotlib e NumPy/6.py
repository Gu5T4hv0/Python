import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1,11)
growth = np.array([30, 35, 42, 48, 53, 60, 62, 67, 75, 80])

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12, 5))

ax1.plot(years, growth)
ax1.set_title("Population Growth Over 10 Years")
ax1.set_xlabel("Years")
ax1.set_ylabel("Population")

ax2.pie(growth, labels=years)
ax2.set_title("Relative Participation of Each Year")

plt.show()