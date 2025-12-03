import pytest
from algo_project.c16_greedy import jump_to_the_end


import pytest

# Test 1: reachable case
def test_jump_to_the_end_reachable():
    nums = [2, 3, 1, 1, 4]
    # Explanation: 0 -> 1 -> 4 (reachable)
    expected = True
    assert jump_to_the_end(nums) == expected


# Test 2: unreachable case
def test_jump_to_the_end_unreachable():
    nums = [3, 2, 1, 0, 4]
    # Explanation: stuck at index 3 (value=0)
    expected = False
    assert jump_to_the_end(nums) == expected

