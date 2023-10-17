# The following arrays are given: A, B.
# Check which numbers (element-wise) from the A array are greater than numbers from the B array 
# and print result to the console as shown below.

# Expected result:
#     [ True False False False]

import numpy as np

A = np.array([0.4, 0.5, 0.3, 0.9])
B = np.array([0.38, 0.51, 0.3, 0.91])

print(A > B)

#Solucion 2 = print(np.greater(A, B))