# The following array:
#     array([[0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0]])
# transform to the following:
#     array([[10,  0, 10,  0, 10,  0],
#            [ 5,  0,  5,  0,  5,  0],
#            [10,  0, 10,  0, 10,  0],
#            [ 5,  0,  5,  0,  5,  0],
#            [10,  0, 10,  0, 10,  0],
#            [ 5,  0,  5,  0,  5,  0]])
# In response, print transformed array to the console.
# Expected output:
#     [[10  0 10  0 10  0]
#      [ 5  0  5  0  5  0]
#      [10  0 10  0 10  0]
#      [ 5  0  5  0  5  0]
#      [10  0 10  0 10  0]
#      [ 5  0  5  0  5  0]]

import numpy as np

a = np.zeros(shape=(6, 6), dtype=int)
a[::2, ::2] = 10
a[1::2, ::2] = 5
print(a)