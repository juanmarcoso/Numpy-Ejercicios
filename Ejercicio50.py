# The following array is given:
#     image = np.random.randint(
#         low=0, high=256, size=(10, 10, 3), dtype=np.uint8
#     )
# Extract any array of shape (5, 5, 3) from this array and assign to the result variable.

import numpy as np

image = np.random.randint(
    low=0, high=256, size=(10, 10, 3), dtype=np.uint8
)

#Comienzo de la resolucion del problema

result = image[:5, :5, :]

# Con estos print quiero comparar los arrays armados previamente y los nuevos array- 
print(image)
print("********************************")
print(result)