# The following arrays are given:
#     A = np.arange(8).reshape(-1, 4)
#     B = np.array([[9, 10, 11, 3],
#                   [2, 8, 0, 9]])      
# Extract the same elements (intersection) of the arrays as a list and print result to the console.
# Expected result:
#     [0 2 3]

import numpy as np

a = np.arange(8).reshape(-1, 4)
b = np.array([[9, 10, 11, 3], [2, 8, 0, 9]])

print(np.intersect1d(a, b))


