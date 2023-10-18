# The following array is given:
#     A = np.array([[0.4], [0.9], [0.5], [0.6]])
# Shape of this array is (4, 1). Remove the unnecessary dimension and extract (4, ) array and print result to the console.
# Expected output:
#     [0.4 0.9 0.5 0.6]

import numpy as np

A = np.array([[0.4], [0.9], [0.5], [0.6]])
A = np.squeeze(A)[()]

print(A)

#Otra solucion ==> print(np.squeeze(A))