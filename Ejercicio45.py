# The following array is given:
#     A = np.array([[[1, 2, 3], [6, 3, 2]]])
# Shape of this array is (1, 2, 3). 
# Remove the unnecessary first dimension and extract (2, 3) array and print it to the console as shown below.
# Expected result:
#     [[1 2 3]
#      [6 3 2]]

import numpy as np

A = np.array([[[1, 2, 3], [6, 3, 2]]])

print(np.squeeze(A, axis=0))

# Segunda opcion ==> print(np.squeeze(A))
