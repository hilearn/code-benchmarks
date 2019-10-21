import math


def _convert_to_psql(x):
    if math.isfinite(x):
        return f'{x:.4f}'
    if math.isnan(x):
        return "'NaN'"
    if math.isinf(x):
        if x > 0:
            return "FLOAT8 'Infinity'"
        else:
            return "FLOAT8 '-Infinity'"
    if x is None:
        return "'null'"


def convert_to_string(a):
    return 'ARRAY[' + ','.join([_convert_to_psql(x) for x in a]) + ']'
