# Using Numpy create a two-dimensional array with shape of (200, 300) 
# filled with random values from 0 to 255 (inclusive) 
# with data type np.uint8 and assign to the variable image.

import numpy as np

image = np.random.randint(
    low=0, high=256, size=(200, 300), dtype=np.uint8
)

print(image)