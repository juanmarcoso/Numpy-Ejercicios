# The following array is given:
#     image = np.random.randint(
#         low=0, high=256, size=(200, 300), dtype=np.uint8
#     )
# Sort this array along the rows in ascending order and assign to the variable image_sorted.

import numpy as np

image = np.random.randint(
    low=0, high=256, size=(200, 300), dtype=np.uint8
)

image_sorted = np.sort(image)

print(image_sorted)