import pytest
from algo_project.c9_intervals import Interval, merge_overlapping_intervals


def test_merge_overlapping_intervals_basic():
    """Test merging overlapping Interval objects."""
    intervals = [
        Interval(1, 3),
        Interval(2, 6),
        Interval(8, 10),
        Interval(15, 18)
    ]
    result = merge_overlapping_intervals(intervals)
    expected = [Interval(1, 6), Interval(8, 10), Interval(15, 18)]

    # Compare by start/end values
    assert [(i.start, i.end) for i in result] == [(e.start, e.end) for e in expected]


def test_merge_no_overlap():
    """Test when no intervals overlap."""
    intervals = [
        Interval(1, 2),
        Interval(3, 4),
        Interval(5, 6)
    ]
    result = merge_overlapping_intervals(intervals)
    expected = [Interval(1, 2), Interval(3, 4), Interval(5, 6)]

    assert [(i.start, i.end) for i in result] == [(e.start, e.end) for e in expected]