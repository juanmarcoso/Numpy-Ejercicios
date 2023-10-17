# Using Numpy create the following two-dimensional array:
#     [[0 0 0 0 0 0]
#      [0 1 0 0 0 0]
#      [0 0 2 0 0 0]
#      [0 0 0 3 0 0]
#      [0 0 0 0 4 0]
#      [0 0 0 0 0 5]]
# Print result to the console as shown below.

import numpy as np

print(np.diag(np.arange(6)))

'''
x = np.arange(36).reshape((6,6))
print(np.diag(np.diag(x)))
'''
