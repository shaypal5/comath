"""array-related utility functions."""

from math import (
    floor,
    ceil,
)


def ndarray_1d_to_int_list(ndarr):
    """Converts a 1-dimensional ndarray to a list of native Python ints.

    Arguments
    ---------
    ndarr : ndarray
        An 1d np.ndarray object with int-convertible items.

    Returns
    -------
    list
        The list of corresponding int objects.
    """
    return [int(x) for x in ndarr]


def percentile(sorted_list, percent, key=lambda x: x):
    """Find the percentile of a sorted list of values.

    Arguments
    ---------
    sorted_list : list
        A sorted list of values.
    percent : float
        A float value from 0.0 to 1.0.
    key : function, optional
        An optional function to compute a value from each element of N.

    Returns
    -------
    The desired percentile of the value list.
    """
    if not sorted_list:
        return None
    k = (len(sorted_list)-1) * percent
    flr = floor(k)
    cil = ceil(k)
    if flr == cil:
        return key(sorted_list[int(k)])
    di0 = key(sorted_list[int(flr)]) * (cil-k)
    di1 = key(sorted_list[int(cil)]) * (k-flr)
    return di0 + di1


def median(sorted_list, key=lambda x: x):
    """Find the median of a sorted list of values.

    Arguments
    ---------
    sorted_list : list
        A sorted list of values.
    key : function, optional
        An optional function to compute a value from each element of N.

    Returns
    -------
    The median of the value list.
    """
    return percentile(sorted_list, 0.5, key)
