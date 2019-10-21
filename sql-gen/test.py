import pure_convert
import numpy_convert
import numpy as np
from time import time

a = list(np.random.normal(0.1, 0.1, 100000))


for f in [pure_convert.convert_to_string,
          numpy_convert.convert_to_string]:
    tsum = 0
    for i in range(30):
        t1 = time()
        f(a)
        t2 = time()
        tsum += t2 - t1
    print(f.__module__, tsum / 10)
