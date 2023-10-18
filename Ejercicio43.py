# The following array is given:
#     image = np.random.randint(
#         low=0, high=256, size=(200, 300, 3), dtype=np.uint8
#     )
# Extend this array by one dimension (add a new dimension at the beginning) and assign to image_extended variable. Expected shape of this array is (1, 200, 300, 3).
# Tip: Use the np.expand_dims() function.

import numpy as np

image = np.random.randint(
    low=0, high=256, size=(200, 300, 3), dtype=np.uint8
)

image_extended = np.expand_dims(image, axis=0)

print(image_extended)
