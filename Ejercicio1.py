# Check if all elements from the following arrays return the logical value True:
# Expected result:
#     A: True
#     B: False
#     C: False
#     D: True

import numpy as np


A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

#Solucion
for name, array in zip(list('ABCD'), [A, B, C, D]): #Creamos una lista y le decimos que la arme con los arrays
    print(f'{name}: {np.all(array)}')