# The following  array is given:
#     array(
#         [
#             [ 0,  1,  2,  3],
#             [ 4,  5,  6,  7],
#             [ 8,  9, 10, 11]
#         ]
#     )
# Using the slice operator, transform this array into the following:
#     array(
#         [
#             [11, 10,  9,  8],
#             [ 7,  6,  5,  4],
#             [ 3,  2,  1,  0]
#         ]
#     )
# In response, print transformed array to the console.
# Expected result:
#     [[11 10  9  8]
#      [ 7  6  5  4]
#      [ 3  2  1  0]]

import numpy as np

A = np.arange(12, dtype='int').reshape(-1, 4)

#Resolucion del problema
print(A[::-1, ::-1])