# Combine the following arrays into one as shown below and print it to the console.
# A = np.arange(12).reshape(-1, 4)
# B = np.array([[4, 3, 7, 2],
#             [0, 5, 2, 6]])
# Expected result:
#     [[ 0  1  2  3]
#      [ 4  5  6  7]
#      [ 8  9 10 11]
#      [ 4  3  7  2]
#      [ 0  5  2  6]]

import numpy as np

A = np.arange(12).reshape(-1, 4)
B = np.array([[4, 3, 7, 2],
            [0, 5, 2, 6]])

print(np.append(A, B, axis=0))