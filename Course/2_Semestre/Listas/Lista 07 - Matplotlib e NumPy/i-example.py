import numpy as np
from PIL import Image

# Create a sample grayscale NumPy array
grayscale_data = np.array([
    [0, 50, 100],
    [150, 200, 255]
], dtype=np.uint8)

# Convert to PIL Image
pil_image = Image.fromarray(grayscale_data, 'L') # 'L' mode for grayscale

# Display or save the image
pil_image.show()
pil_image.save('grayscale_image_pil.png')