"""Utility pure-Python 3 decorators."""

import comath.array
import comath.func
import comath.metric
import comath.segment
try:
    del comath
except NameError: # pragma: no cover
    pass

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
