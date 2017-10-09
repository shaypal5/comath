"""Defines a one-dimensional line segment."""

from math import (
    inf,
)


class LineSegment(object):
    """Defines a one-dimensional line segment."""

    @staticmethod
    def _parse_edge(edge):
        if isinstance(edge, (int, float)):
            return edge
        if isinstance(edge, str):
            if edge in ['inf', 'infinity']:
                return inf
            if edge in ['-inf', '-infinity']:
                return -inf
            try:
                return float(edge)
            except ValueError:
                pass
        raise ValueError(
            "Bad type for edge of LineSegment. Allowed types are int, float,"
            " parsable strings and inf/-inf/infinity/-infinity.")

    def __init__(self, left_edge, right_edge, left_inclusive=True,
                 right_inclusive=True):
        self.left_edge = self._parse_edge(left_edge)
        self.right_edge = self._parse_edge(right_edge)
        self.left_inclusive = left_inclusive
        self.right_inclusive = right_inclusive
        if self.left_inclusive:
            self.left_test = lambda x: x >= self.left_edge
        else:
            self.left_test = lambda x: x > self.left_edge
        if self.right_inclusive:
            self.right_test = lambda x: x <= self.right_edge
        else:
            self.right_test = lambda x: x < self.right_edge

    def __contains__(self, key):
        try:
            return self.left_test(key) and self.right_test(key)
        except TypeError:
            return False

    def contains(self, number):
        """Returns True if the given number is contained in this segment."""
        return number in self

    TYPE_ERR_MSG = "Bad type for intersection with LineSegment: {}"

    def __and__(self, other):
        if hasattr(other, '__iter__') and not isinstance(other, str):
            return set(member for member in other if member in self)
        raise TypeError(self.TYPE_ERR_MSG.format(type(other)))

    def intersection(self, other):
        """Returns a set of all elements of other contained in this segment."""
        return self & other
