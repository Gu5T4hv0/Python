import numpy as np
x = np.array([10, 20, 30, 40])
high = x[x>25]
print(high)

a = np.array([1,2,3,4])
power = a**2
print(power)

x = np.array([[1,2],[3,4]])
ravel = x.ravel()
print(ravel)

dados = np.array([1,2,3,4,5,6])
data = dados[::2]
print(data)