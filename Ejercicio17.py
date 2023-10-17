# The following array is given:
#     A = np.array([[1, 4, 3],
#                   [5, 2, 6]])
# Iterate through this array and print each element to the console.

# Expected result:
#     1
#     4
#     3
#     5
#     2
#     6

import numpy as np

A = np.array([[1, 4, 3],[5, 2, 6]])

for i in np.nditer(A):
    print(i)