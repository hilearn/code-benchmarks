cimport numpy as np
from libcpp.string cimport string

def convert_to_string(np.ndarray[np.float64_t, ndim=1] a):
    cdef string ret = "ARRAY["
    for i in range(999):
        if a[i] is None:
            ret.append("'null',")
        else:
            ret.append(<string>str.encode(f'{a[i]:.4f},'))
    if a[999] is None:
        ret.append("'null']")
    else:
        ret.append(<string>str.encode(f'{a[999]:.4f}]'))
    return ret