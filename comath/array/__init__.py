"""array-related utility functions."""

from .array import (
    ndarray_1d_to_int_list,
    percentile,
    median,
)
try:
    del array
except NameError:
    pass
