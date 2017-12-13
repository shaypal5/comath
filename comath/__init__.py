"""Utility pure-Python 3 decorators."""

from . import (
    array,
    func,
    metric,
    segment,
)
# try:
#     del comath
# except NameError: # pragma: no cover
#     pass

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
