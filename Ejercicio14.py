# Set the random seed to 10. Then using Numpy create a one-dimensional array consisting of 
# 30 pseudo-randomly generated values from the uniform distribution [0,1). 
# Print result to the console as shown below.

# Expected result:
#     [0.77132064 0.02075195 0.63364823 0.74880388 0.49850701 0.22479665
#      0.19806286 0.76053071 0.16911084 0.08833981 0.68535982 0.95339335
#      0.00394827 0.51219226 0.81262096 0.61252607 0.72175532 0.29187607
#      0.91777412 0.71457578 0.54254437 0.14217005 0.37334076 0.67413362
#      0.44183317 0.43401399 0.61776698 0.51313824 0.65039718 0.60103895]

import numpy as np

np.random.seed(10)
print(np.random.rand(30))