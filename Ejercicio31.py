# The following array is given:
#     A = np.array(
#         [[4.99, 3.49, 9.99], [1.99, 9.99, 4.99], [14.99, 2.39, 7.29]]
#     )
# Sort this array:
#     by row (ascending)
#     by column (ascending)

# And print result to the console as shown below.
# Expected result:
#     [[ 3.49  4.99  9.99]

import numpy as np


A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 4.99],
              [14.99, 2.39, 7.29]])

print(np.sort(A))
print(np.sort(A, axis=0))