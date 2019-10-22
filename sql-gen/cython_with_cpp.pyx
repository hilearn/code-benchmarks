cimport numpy as np
from libcpp.string cimport string

def convert_to_string(np.ndarray[np.float64_t, ndim=1] a):
    cdef string ret = "ARRAY["
    cdef int n = a.shape[0]
    for i in range(n):
        if a[i] is None:
            ret.append("'null'")
        else:
            ret.append(<string>str.encode(f'{a[i]:.4f}'))
        if i == n - 1:
            ret.append("]")
        else:
            ret.append(",")