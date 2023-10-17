# Using Numpy create the following array:
#     array([[ 0,  1,  2,  3],
#            [ 4,  5,  6,  7],
#            [ 8,  9, 10, 11]])

# Save this array to a binary file named 'array.npy' and then load that file back into another variable. 
# Print this variable to the console.

import numpy as np

A = np.arange(12).reshape(-1, 4)
np.save('array.npy', A)
 
B = np.load('array.npy')
print(B)