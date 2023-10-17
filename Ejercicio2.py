# Check if all elements from the following arrays return the logical value True along the axis with index 1:
# Expected result:
#     A: [ True  True]
#     B: [ True False]
#     C: [False  True]

import numpy as np


A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

for name, array in zip(list('ABC'), [A, B, C]):
    print(f'{name}: {np.all(array, axis=1)}')