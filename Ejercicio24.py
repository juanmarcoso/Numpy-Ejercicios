# The following array is given:
#     array([[ 0,  1,  2,  3],
#            [ 4,  5,  6,  7],
#            [ 8,  9, 10, 11]])
# Using the slice operator, transform this array into the following:
#     array([[ 8,  9, 10, 11],
#            [ 4,  5,  6,  7],
#            [ 0,  1,  2,  3]])
# In response, print transformed array to the console.
# Expected output:
#     [[ 8  9 10 11]
#      [ 4  5  6  7]
#      [ 0  1  2  3]]

import numpy as np

a = np.arange(12, dtype=int).reshape(-1, 4)
print(a[::-1])