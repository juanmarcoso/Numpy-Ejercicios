# Using Numpy create a three-dimensional array called image with shape (200, 300, 3) filled with random values from 0 to 255 (inclusive) and data type np.uint8. Set random seed to 42.
# In response, print array to the console.

import numpy as np

np.random.seed(42) # Seteo en cuanto me pide

image = np.random.randint(
    low=0, high=256, size=(200, 300, 3), dtype=np.uint8 # Luego armo la variable y le doy sus atributos
)

print(image)