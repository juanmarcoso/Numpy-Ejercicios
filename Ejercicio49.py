# Random seed is set to 42. The following array is given:
#     image = np.random.randint(
#         low=0, high=256, size=(10, 10, 3), dtype=np.uint8
#     )
# Extract the first channel (index 0) of this image array and print it to the console.
# Expected output:
#     [[102 220 225]
#      [ 95 179  61]
#      [234 203  92]
#      [  3  98 243]
#      [ 14 149 245]
#      [ 46 106 244]
#      [ 99 187  71]
#      [212 153 199]
#      [188 174  65]
#      [153  20  44]]

import numpy as np

np.random.seed(42)

image = np.random.randint(
    low=0, high=256, size=(10, 10, 3), dtype=np.uint8
)

#Resolucion del problema
print(image[0, :])

#Segunda solucion ==> print(image[0, :, :])
