# Using Numpy create a one-dimensional array (vector) consisting of eleven equally distributed 
# numbers from the [0,1] interval.

#Expected result:
#    [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]

import numpy as np

print(np.linspace(start=0, stop=1, num=11))