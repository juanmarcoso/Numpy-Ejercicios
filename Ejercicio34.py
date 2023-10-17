# Present the following two-dimensional array as a flattened one-dimensional array and print result to the console.
#     A = np.array(
#         [
#             [4.99, 3.49, 9.99],
#             [1.99, 9.99, 14.99],
#             [14.99, 2.39, 7.29],
#         ]
#     )
# Tip: Use the np.ravel() function.
# Expected result:
#     [ 4.99  3.49  9.99  1.99  9.99 14.99 14.99  2.39  7.29]

import numpy as np


A = np.array(
    [
        [4.99, 3.49, 9.99],
        [1.99, 9.99, 14.99],
        [14.99, 2.39, 7.29],
    ]
)

print(np.ravel(A))
