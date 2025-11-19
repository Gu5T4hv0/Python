import numpy as np
matriz = np.arange(9).reshape(3,3)
print(matriz[0][0], matriz[-1][-1])

matriz5x5 = np.arange(25).reshape(5,5)
print(matriz5x5)
linha2 = matriz5x5[1]
print(linha2)

print("-"*20)

coluna3 = matriz5x5[:,2]
print(coluna3)

print("-"*20)

central = matriz5x5[1:-1,1:-1]
print(central)