# Using Numpy create a two-dimensional array with the shape (10, 4) 
# pseudo-randomly generated values from the standard normal distribution N(0,1). 
# Set the random seed to 20. Print result to the console as shown below.

# Expected result:
#     [[ 0.88389311  0.19586502  0.35753652 -2.34326191]
#      [-1.08483259  0.55969629  0.93946935 -0.97848104]
#      [ 0.50309684  0.40641447  0.32346101 -0.49341088]
#      [-0.79201679 -0.84236793 -1.27950266  0.24571517]
#      [-0.0441948   1.56763255  1.05110868  0.40636843]
#      [-0.1686461  -3.18970279  1.12013226  1.33277821]
#      [-0.24333877 -0.13003071 -0.10901737  1.55618644]
#      [ 0.12877835 -2.06694872 -0.88549315 -1.10457948]
#      [ 0.93286635  2.059838   -0.93493796 -1.61299022]
#      [ 0.52706972 -1.55110074  0.32961334 -1.13652654]]

import numpy as np

np.random.seed(20)
print(np.random.randn(10, 4))