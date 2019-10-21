import numpy as np


def _convert_to_psql(x):
    if np.isfinite(x):
        return f'{x:.4f}'
    if np.isnan(x):
        return "'NaN'"
    if np.isposinf(x):
        return "FLOAT8 'Infinity'"
    if np.isneginf(x):
        return "FLOAT8 '-Infinity'"
    if x is None:
        return "'null'"


def convert_to_string(arr):
    return 'ARRAY[' + ','.join([_convert_to_psql(x) for x in arr]) + ']'
