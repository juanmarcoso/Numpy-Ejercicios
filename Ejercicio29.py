# The following array is given:
#     A = np.array([[5, 1, 2, 1, 2],
#                   [9, 1, 9, 7, 5],
#                   [4, 1, 5, 7, 9]])
# Extract all unique values of this array as a list and print it to the console.
# Expected result:
#     [1 2 4 5 7 9]

import numpy as np

np.random.seed(10)
A = np.random.randint(low=1, high=10, size=(3, 5))

print(np.unique(A))