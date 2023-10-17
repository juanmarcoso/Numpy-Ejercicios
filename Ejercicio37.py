# Using Numpy create a two-dimensional array (lower triangular matrix):
#     array(
#         [
#             [1., 0., 0., 0., 0.],
#             [1., 1., 0., 0., 0.],
#             [1., 1., 1., 0., 0.],
#             [1., 1., 1., 1., 0.],
#             [1., 1., 1., 1., 1.]
#         ]
#     )
# In response, print result to the console.
# Expected result:
#     [[1. 0. 0. 0. 0.]
#      [1. 1. 0. 0. 0.]
#      [1. 1. 1. 0. 0.]
#      [1. 1. 1. 1. 0.]
#      [1. 1. 1. 1. 1.]]

import numpy as np

print(np.tri(5, 5, dtype=float))

#Segunda opcion => print(np.tri(N=5))