cimport numpy as np
from libc.stdlib cimport malloc
from libc.string cimport strcpy, strcat

cdef extern from "mystring.h":
    char* mystrcat(char* dest, char* src)

ctypedef np.float64_t dtype_t

def convert_to_string(np.ndarray[dtype_t, ndim=1] a):
    cdef char *ret = <char *> malloc(9008)
    cdef char *p = ret
    ret[0]='\0'
    p = mystrcat(p, "ARRAY[")
    for i in range(999):
        if a[i] is None:
            p = mystrcat(p, "'null',")
        else:
            p = mystrcat(p, str.encode(f'{a[i]:.4f},'))
    if a[999] is None:
        p = mystrcat(p, "'null',")
    else:
        p = mystrcat(p, str.encode(f'{a[999]:.4f}]'))
    return ret.decode()