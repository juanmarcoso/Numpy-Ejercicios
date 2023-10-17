# Check if any element of the following arrays returns the logical value True:
# Expected result:
#     A: False
#     B: True
#     C: True
#     D: True

import numpy as np

A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.any(array)}')