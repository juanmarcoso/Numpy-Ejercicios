# The following array:
#     array([[1., 1., 1., 1.],
#            [1., 1., 1., 1.],
#            [1., 1., 1., 1.],
#            [1., 1., 1., 1.]])
# transform to this array:
#     array([[0., 0., 0., 0., 0., 0.],
#            [0., 1., 1., 1., 1., 0.],
#            [0., 1., 1., 1., 1., 0.],
#            [0., 1., 1., 1., 1., 0.],
#            [0., 1., 1., 1., 1., 0.],
#            [0., 0., 0., 0., 0., 0.]])
# In response, print transformed array to the console.
# Expected output:
#     [[0. 0. 0. 0. 0. 0.]
#      [0. 1. 1. 1. 1. 0.]
#      [0. 1. 1. 1. 1. 0.]
#      [0. 1. 1. 1. 1. 0.]
#      [0. 1. 1. 1. 1. 0.]
#      [0. 0. 0. 0. 0. 0.]]

import numpy as np

x = np.ones([4,4])
y = np.pad(x, 1)
print(y)

'''
Solucion alt = 
A = np.ones(shape=(4, 4))
print(np.pad(A, pad_width=1, constant_values=0))
'''