import pytest
from algo_project.c15_dp import climbing_stairs, min_coin_combination, matrix_pathways


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


# Test 1: basic case where solution exists
def test_min_coin_basic():
    coins = [1, 2, 3]
    target = 5
    # 2 coins -> (2 + 3) or (1 + 2 + 2) but the minimum is 2
    expected = 2
    assert min_coin_combination(coins, target) == expected


# Test 2: no possible combination
def test_min_coin_no_solution():
    coins = [4, 5]
    target = 3
    # Cannot make 3 using 4 or 5, so return -1
    expected = -1
    assert min_coin_combination(coins, target) == expected

import pytest

# Test 1: small known grid sizes
def test_matrix_pathways_basic():
    # 1x1 grid -> 1 path (already at destination)
    # 2x2 grid -> 2 paths: Right->Down, Down->Right
    # 3x3 grid -> 6 paths (classic combinatorics result)
    test_cases = {
        (1, 1): 1,
        (2, 2): 2,
        (3, 3): 6
    }

    for (m, n), expected in test_cases.items():
        assert matrix_pathways(m, n) == expected


# Test 2: rectangular grid
def test_matrix_pathways_rectangular():
    # 3x7 grid should have C(3+7-1, 3-1) = C(9,2) = 36 unique paths
    m = 3
    n = 7
    expected = 28
    assert matrix_pathways(m, n) == expected

    m = 3
    n = 4
    expected = 10
    assert matrix_pathways(m, n) == expected