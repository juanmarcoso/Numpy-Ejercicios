# Using Numpy, create an array 10x10 filled with number 255 and set the data type to float. 
# Print this array to the console as shown below.
# Expected result:
#     [[255. 255. 255. 255. 255. 255. 255. 255. 255. 255.]
#      [255. 255. 255. 255. 255. 255. 255. 255. 255. 255.]
#      [255. 255. 255. 255. 255. 255. 255. 255. 255. 255.]
#      [255. 255. 255. 255. 255. 255. 255. 255. 255. 255.]
#      [255. 255. 255. 255. 255. 255. 255. 255. 255. 255.]
#      [255. 255. 255. 255. 255. 255. 255. 255. 255. 255.]
#      [255. 255. 255. 255. 255. 255. 255. 255. 255. 255.]
#      [255. 255. 255. 255. 255. 255. 255. 255. 255. 255.]
#      [255. 255. 255. 255. 255. 255. 255. 255. 255. 255.]
#      [255. 255. 255. 255. 255. 255. 255. 255. 255. 255.]]

import numpy as np

y = (10, 10)
x = np.full(y, fill_value=255, dtype=float)

print(x)

#Solucion 2 = print(np.ones(shape=(10, 10), dtype='float') * 255)
#Solucion 3 = print(np.full(shape=(10, 10), fill_value=255, dtype='float'))