# Check if the following arrays are equal (element-wise):
# Expected result:
#     True

import numpy as np

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])

print(np.allclose(A,B))