import pytest
from algo_project.c9_intervals import Interval, merge_overlapping_intervals, identify_all_interval_overlaps, largest_overlap_of_intervals


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
    
def test_basic_overlaps_identify_all_interval_overlaps():
    """Test overlapping intervals between two lists."""
    intervals1 = [Interval(1, 5), Interval(10, 14), Interval(16, 18)]
    intervals2 = [Interval(3, 7), Interval(12, 15), Interval(17, 20)]

    result = identify_all_interval_overlaps(intervals1, intervals2)
    expected = [Interval(3, 5), Interval(12, 14), Interval(17, 18)]

    assert [(i.start, i.end) for i in result] == [(e.start, e.end) for e in expected]


def test_no_overlap_identify_all_interval_overlaps():
    """Test when there are no overlapping intervals."""
    intervals1 = [Interval(1, 2), Interval(5, 6)]
    intervals2 = [Interval(3, 4), Interval(7, 8)]

    result = identify_all_interval_overlaps(intervals1, intervals2)
    assert result == []
    
def test_basic_overlap():
    intervals = [
        Interval(1, 5),
        Interval(2, 6),
        Interval(4, 8),
        Interval(7, 9)
    ]

    # Max overlap is 3 between [4,5)
    assert largest_overlap_of_intervals(intervals) == 3
    
def test_half_open_and_no_overlap():
    # Half-open means [1,2), [2,3), [3,4) do NOT overlap
    intervals = [
        Interval(1, 2),
        Interval(2, 3),
        Interval(3, 4)
    ]

    assert largest_overlap_of_intervals(intervals) == 1