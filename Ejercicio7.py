# Check if the following arrays are equal (element-wise):
# Expected result:
#     [False False  True]

import numpy as np

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])

for array in list([A, B]):
    x = A == B
    
print(x)

#Solucion 2 = print(np.equal(A, B))
#Solucion 3 = print(A == B)