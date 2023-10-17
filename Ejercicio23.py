# Using Numpy create and convert the following array into the list:
#     array([[ 0,  1,  2,  3],
#            [ 4,  5,  6,  7],
#            [ 8,  9, 10, 11]])
# In response, print list to the console.
# Expected output:
#     [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

import numpy as np

A = np.arange(12).reshape(-1, 4)
B = A.tolist()

print(B)

'''
Alternativa =
A = np.arange(12, dtype='int').reshape(-1, 4)
print(A.tolist())
'''
