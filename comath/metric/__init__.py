"""metric-related utility functions."""

from .metric import (
    MovingMetricTracker,
    MovingAverageTracker,
    MovingVarianceTracker,
    MovingPrecisionTracker,
)
try:
    del metric
except NameError:
    pass
