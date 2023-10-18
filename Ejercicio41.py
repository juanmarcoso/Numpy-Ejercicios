# The following array is given:
#     A = np.array([[4, 2, 1],
#                   [6, 4, 2]])
# Expand this array by one dimension (add a new dimension at the beginning). Expected shape of the output array: (1, 2, 3).
# In response, print array to the console.
# Expected output:
#     [[[4 2 1]
#       [6 4 2]]]

import numpy as np


A = np.array([[4, 2, 1],
              [6, 4, 2]])

print(np.expand_dims(A, axis=0))


