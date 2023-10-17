# The following array is given:
#     A = np.array(
#         [
#             [4.99, 3.49, 9.99],
#             [1.99, 9.99, 14.99],
#             [14.99, 2.39, 7.29],
#         ]
#     )
# Replace elements greater than 10 with a fixed value = 10.0 and print result to the console.
# Expected result:
#     [[ 4.99  3.49  9.99]
#      [ 1.99  9.99 10.  ]
#      [10.    2.39  7.29]]

import numpy as np


A = np.array(
    [
        [4.99, 3.49, 9.99],
        [1.99, 9.99, 14.99],
        [14.99, 2.39, 7.29],
    ]
)
print(np.where(A < 10.00, A, 10.00))

#Segunda solucion == print(np.where(A > 10.0, 10.0, A))

