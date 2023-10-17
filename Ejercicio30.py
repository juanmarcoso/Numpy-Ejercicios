# The following array is given:
#     A = np.array([[0.4, 0.3, 0.3],
#                   [0.1, 0.1, 0.8],
#                   [0.2, 0.5, 0.3]])
# Return a list of indexes with maximum values for each row from this array and print it to the console.
# Expected result:
#     [0 2 1]

import numpy as np

A = np.array([[0.4, 0.3, 0.3],
                [0.1, 0.1, 0.8],
                [0.2, 0.5, 0.3]])

print(np.argmax(A, axis=1, keepdims=False))