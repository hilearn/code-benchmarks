import numpy as np


def convert_to_string(arr):
    return np.array2string(arr, precision=4, separator=',', prefix='ARRAY[', suffix=']')
