# Using Numpy create a one-dimensional array (vector) containing the possible result from the Big Lotto game. 
# Set the random seed to 42. Print result to the console.

# Expected result:
#     [14 46 48 45 18 28]

import numpy as np

np.random.seed(42)
print(np.random.choice(range(1, 50), size=6, replace=False))