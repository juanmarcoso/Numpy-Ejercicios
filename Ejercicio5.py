# Check if the following array has missing data:
# Expected result:
#     [[False False False  True]
#      [False  True False False]]

import numpy as np

A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])

print(np.isnan(A))