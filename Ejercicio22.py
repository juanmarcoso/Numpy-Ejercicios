# Using Numpy create the following array:
#     array([[ 0,  1,  2,  3],
#            [ 4,  5,  6,  7],
#            [ 8,  9, 10, 11]])

# Save this array to a text file named 'array.txt' with two decimal places and then load this file back 
# into another variable. Print this variable to the console.

import numpy as np

A = np.arange(12, dtype=int).reshape(-1, 4)
np.savetxt(fname='array.npy', X=A, fmt='%0.2f')
 
B = np.loadtxt('array.npy')
print(B)