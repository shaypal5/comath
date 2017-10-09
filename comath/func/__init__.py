"""function-related utility functions."""

from .func import (
    get_smooth_step_function,
    closest_larger_power_of_2,
)
try:
    del func
except NameError:
    pass
