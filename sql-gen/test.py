import pure_convert
import numpy_array2string
import numpy_naive
from pure_class_convert import ConstantLengthExporter
import numpy as np
from time import time

a = np.random.normal(0.1, 0.1, 1000)
N = 300

for f in [pure_convert.convert_to_string,
          numpy_array2string.convert_to_string,
          numpy_naive.convert_to_string]:
    tsum = 0
    for i in range(N):
        t1 = time()
        f(a)
        t2 = time()
        tsum += t2 - t1
    print(f.__module__, tsum / N)
