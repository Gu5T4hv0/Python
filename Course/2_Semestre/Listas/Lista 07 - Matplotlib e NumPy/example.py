import matplotlib.pyplot as plt
import numpy as np
# x = [1, 2, 3, 4]
# y = [2, 4, 6, 8]

# plt.plot(x,y)
# plt.title("Simple line plot")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.show()


x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]

plt.plot(x, y1, label="Squared")
plt.plot(x, y2, label="Linear")
plt.legend()
plt.show()
