# Using Numpy create a two-dimensional array with the shape (10, 4) 
# pseudo-randomly generated values from the normal distribution N(100, 5). 
# Set the random seed to 30. Print result to the console as shown below.

# Expected result:
#     [[ 97.17349231 103.41650023  97.82942436 101.05220329]
#      [ 99.7748353  100.67930221  96.14063068 103.544381  ]
#      [100.30029631  97.52499594 103.52901961 100.24037271]
#      [ 98.29153712  98.2666258  103.09437633 101.70027274]
#      [ 99.36127721 101.20382627  95.34026547 102.09694365]
#      [ 99.98708001  98.95468525  99.05410904 102.38025432]
#      [ 93.50787269 103.61547679 103.18753701  98.51356237]
#      [102.20256689  96.19764407  97.54000366  97.05813038]
#      [101.81233513  97.66380453  98.45883627  98.09317768]
#      [102.48979932  95.70413391  98.43161651 101.89861815]]

import numpy as np

np.random.seed(30)
 
sigma = np.sqrt(5)
mu = 100
 
print(sigma * np.random.randn(10, 4) + mu)