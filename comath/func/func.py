"""function-related utility functions."""

from math import (
    tanh,
    ceil,
    log2,
)


def get_smooth_step_function(min_val, max_val, switch_point, smooth_factor):
    """Returns a function that moves smoothly between a minimal value and a
    maximal one when its value increases from a given witch point to infinity.

    Arguments
    ---------
    min_val: float
        max_val value the function will return when x=switch_point.
    min_val: float
        The value the function will converge to when x -> infinity.
    switch_point: float
        The point in which the function's value will become min_val. Smaller
        x values will return values smaller than min_val.
    smooth_factor: float
        The bigger the smoother, and less cliff-like, is the function.

    Returns
    -------
    function
        The desired smooth function.
    """
    dif = max_val - min_val
    def _smooth_step(x):
        return min_val + dif * tanh((x - switch_point) / smooth_factor)
    return _smooth_step


def closest_larger_power_of_2(number):
    """Returns the closest power of 2 that is larger than the given number."""
    try:
        return pow(2, ceil(log2(number)))
    except ValueError:
        return 1
