cimport numpy as np
from libc.stdlib cimport malloc
from libc.string cimport strcpy, strcat

cdef extern from "mystring.h":
    char* mystrcat(char* dest, char* src)

ctypedef np.float64_t dtype_t

def convert_to_string(np.ndarray[dtype_t, ndim=1] a):
    cdef char *ret = <char *> malloc(9008)
    cdef char *p = ret
    cdef int n = a.shape[0]
    ret[0]='\0'
    p = mystrcat(p, "ARRAY[")
    for i in range(n):
        if a[i] is None:
            p = mystrcat(p, "'null'")
        else:
            p = mystrcat(p, str.encode(f'{a[i]:.4f}'))
        if i == n - 1:
            p = mystrcat(p, "]")
        else:
            p = mystrcat(p, ",")
    return ret.decode()