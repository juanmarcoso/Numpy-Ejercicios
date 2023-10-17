# Using Numpy create a 4x4 array filled with zeros (set data type to int). In response print 
# this array to the console.
# Expected result:
#     [[0 0 0 0]
#      [0 0 0 0]
#      [0 0 0 0]
#      [0 0 0 0]]

import numpy as np

y = (4,4)
x = np.zeros(y, dtype=int)

print(x)

#Solucion 2 = print(np.zeros(shape=(4, 4), dtype='int'))