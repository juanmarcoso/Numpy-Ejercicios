# Two randomly generated arrays are given:
#     image1 = np.random.randint(
#         low=0, high=256, size=(200, 300, 3), dtype=np.uint8
#     )
#     image2 = np.random.randint(
#         low=0, high=256, size=(200, 300, 3), dtype=np.uint8
#     )
# Expand each of these arrays by adding one dimension at the beginning and then combine these arrays into one called images. Expected shape of images array: (2, 200, 300, 3).

import numpy as np

image1 = np.random.randint(
    low=0, high=256, size=(200, 300, 3), dtype=np.uint8
)
image2 = np.random.randint(
    low=0, high=256, size=(200, 300, 3), dtype=np.uint8
)

image1 = np.expand_dims(image1, axis=0)
image2 = np.expand_dims(image2, axis=0)

images = np.append(image1, image2, axis=0)

print(images)