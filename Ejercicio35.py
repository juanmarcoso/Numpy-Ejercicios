# The following array is given:
#     A = np.array(
#         [
#             [4.99, 3.49, 9.99],
#             [1.99, 9.99, 14.99],
#             [14.99, 2.39, 7.29],
#         ]
#     )
# Using Numpy create an array of the same shape and data type as the given array and fill it with zeros. Print this array to the console.
# Expected result:
#     [[0. 0. 0.]
#      [0. 0. 0.]
#      [0. 0. 0.]]

import numpy as np


A = np.array(
    [
        [4.99, 3.49, 9.99],
        [1.99, 9.99, 14.99],
        [14.99, 2.39, 7.29],
    ]
)

print(np.zeros_like(A))