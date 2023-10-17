# Using Numpy create a 6x6 two-dimensional array - identity matrix with int data type. 
# Print this array to the console as shown below.
# Expected result:
    # [[1 0 0 0 0 0]
    #  [0 1 0 0 0 0]
    #  [0 0 1 0 0 0]
    #  [0 0 0 1 0 0]
    #  [0 0 0 0 1 0]
    #  [0 0 0 0 0 1]]

import numpy as np

print(np.eye(6, k=0, dtype=int))

# solucion alt = print(np.eye(N=6, dtype='int'))