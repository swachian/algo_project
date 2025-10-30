import pytest
from algo_project.c1_two_pointers import pair_sum_sorted

def test_two_sum_found():
    nums = [1, 2, 3, 4, 6]
    target = 6
    result = pair_sum_sorted(nums, target)
    # Either [1,3] or [3,1] is acceptable, so we sort it before checking
    assert sorted(result) == [1, 3]

def test_two_sum_no_pair():
    nums = [1, 2, 3, 9]
    target = 8
    result = pair_sum_sorted(nums, target)
    assert result == []

def test_two_sum_first_last():
    nums = [1, 5, 9, 10]
    target = 11
    result = pair_sum_sorted(nums, target)
    assert sorted(result) == [0, 3]
