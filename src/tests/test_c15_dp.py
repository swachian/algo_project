import pytest
from algo_project.c15_dp import climbing_stairs


# Test 1: small known values (Fibonacci-like behavior)
def test_climbing_stairs_basic():
    # n=1 -> 1 way (1)
    # n=2 -> 2 ways (1+1, 2)
    # n=3 -> 3 ways (1+1+1, 1+2, 2+1)
    expected_results = {1: 1, 2: 2, 3: 3}
    for n, expected in expected_results.items():
        assert climbing_stairs(n) == expected


# Test 2: larger value to ensure correct recurrence
def test_climbing_stairs_larger_n():
    # Known result: n=10 -> 89 ways
    n = 10
    expected = 89  # Based on Fibonacci pattern
    assert climbing_stairs(n) == expected
