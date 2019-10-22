import pure_convert
import numpy_array2string
import numpy_naive
import cython_with_c
import cython_with_cpp
import numpy as np
from time import time
import random

a = np.random.normal(0.1, 0.1, 1000)
for i in range(10):
    a[random.randrange(1000)] = None
N = 300

for f in [pure_convert.convert_to_string,
          numpy_array2string.convert_to_string,
          numpy_naive.convert_to_string,
          cython_with_c.convert_to_string,
          cython_with_cpp.convert_to_string]:
    tsum = 0
    for i in range(N):
        t1 = time()
        f(a)
        t2 = time()
        tsum += t2 - t1
    print(f.__module__, tsum / N)
