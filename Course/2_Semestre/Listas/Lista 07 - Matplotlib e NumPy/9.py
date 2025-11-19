from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

gray = np.array(Image.open('quebra codigos gray.png'))
inverted_value = 255 - gray

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12, 5))
ax1.imshow(gray, cmap='gray')
ax2.imshow(inverted_value, cmap='gray')
plt.show()