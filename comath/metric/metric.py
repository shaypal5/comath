"""metric-related utility functions."""

import abc


class MovingMetricTracker(metaclass=abc.ABCMeta):
    """An object that tracks and computes a moving metric."""

    def __init__(self, metric_name):
        self.metric_name = metric_name

    @abc.abstractmethod
    def add_value(self, value):
        """Incorporate a new value into the metric tracker.

        Arguments
        ---------
        value : float
            Add a new value of the metric.
        """
        pass

    @abc.abstractmethod
    def get_metric(self):
        """Get the value of the metric."""
        pass


class MovingAverageTracker(MovingMetricTracker):
    """An object that tracks and computes a moving average."""

    def __init__(self, metric_name=None):
        MovingMetricTracker.__init__(
            self,
            metric_name=metric_name or 'Average'
        )
        self.val_sum = 0
        self.n = 0

    def add_value(self, value):
        self.val_sum += value
        self.n += 1

    def get_metric(self):
        try:
            return self.val_sum / self.n
        except ZeroDivisionError:
            return 0


class MovingVarianceTracker(MovingMetricTracker):
    """An object that tracks and computes a moving variance measure.

    Uses Welford's Algorithm:
    https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm
    """

    def __init__(self, metric_name=None):
        MovingMetricTracker.__init__(
            self,
            metric_name or 'Variance'
        )
        self.n = 0
        self.delta = 0
        self.delta2 = 0
        self.mean = 0
        self.m2k = 0

    def add_value(self, value):
        self.n += 1
        self.delta = value - self.mean
        self.mean += self.delta / self.n
        self.delta2 = value - self.mean
        self.m2k += self.delta * self.delta2

    def get_metric(self):
        if self.n < 2:
            return None
        else:
            return self.m2k / (self.n - 1)


class MovingPrecisionTracker(MovingMetricTracker):
    """An object that tracks and computes a moving precision measure."""

    def __init__(self, metric_name=None):
        MovingMetricTracker.__init__(
            self,
            metric_name or 'Precision'
        )
        self.true_count = 0
        self.n = 0

    def add_value(self, value):
        if value:
            self.true_count += 1
        self.n += 1

    def get_metric(self):
        try:
            return self.true_count / self.n
        except ZeroDivisionError:
            return 0
