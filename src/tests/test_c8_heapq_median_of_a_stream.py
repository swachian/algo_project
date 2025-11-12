import pytest
from algo_project.c8_heapq_median_of_a_stream import MedianOfAnIntegerStream

def test_basic_median_sequence():
    """Test median calculation as numbers are added sequentially."""
    stream = MedianOfAnIntegerStream()
    stream.add(1)
    stream.add(2)
    assert stream.get_median() == 1.5  # (1 + 2) / 2
    stream.add(3)
    assert stream.get_median() == 2.0  # middle element is 2

def test_unordered_input():
    """Test with numbers added in random order."""
    stream = MedianOfAnIntegerStream()
    for num in [5, 15, 1, 3]:
        stream.add(num)
    # Sorted order: [1, 3, 5, 15] → median = (3 + 5)/2 = 4.0
    assert stream.get_median() == 4.0