import pytest
from algo_project.c15_dp import climbing_stairs, min_coin_combination, matrix_pathways, neighborhood_burglary, longest_common_subsequence, longest_palindrome_in_a_string, maximum_subarray_sum, knapsack, largest_square_in_a_matrix


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
    n = 4
    expected = 5  # Based on Fibonacci pattern
    assert climbing_stairs(n) == expected


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
    

# Test 1: basic scenario with several non-adjacent choices
def test_neighborhood_burglary_basic():
    houses = [2, 7, 9, 3, 1]
    # Optimal: rob house 1 (2), house 3 (9), house 5 (1) = 12
    # Or rob house 2 (7) and house 4 (3) = 10
    expected = 12
    assert neighborhood_burglary(houses) == expected


# Test 2: edge case with adjacent large values
def test_neighborhood_burglary_adjacent_large():
    houses = [10, 1, 10]
    # Best is rob first and third house = 20
    expected = 20
    assert neighborhood_burglary(houses) == expected


# Test 1: classic known example
def test_lcs_classic():
    s1 = "ABCBDAB"
    s2 = "BDCAB"
    # One LCS is "BCAB" or "BDAB" → length = 4
    expected = 4
    assert longest_common_subsequence(s1, s2) == expected


# Test 2: completely different strings
def test_lcs_no_common_subsequence():
    s1 = "AAAA"
    s2 = "BBBB"
    # No common characters → LCS length = 0
    expected = 0
    assert longest_common_subsequence(s1, s2) == expected



# Test 1: classic example with a clear longest palindrome
def test_longest_palindrome_basic():
    s = "babad"
    # Valid answers are "bab" or "aba" (both length 3)
    result = longest_palindrome_in_a_string(s)
    assert result in ("bab", "aba")


# Test 2: fully palindromic string
def test_longest_palindrome_full_string():
    s = "racecar"
    # Entire string is the longest palindrome
    expected = "racecar"
    assert longest_palindrome_in_a_string(s) == expected


# Test 1: classic Kadane example
def test_maximum_subarray_basic():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Maximum subarray is [4, -1, 2, 1] with sum = 6
    expected = 6
    assert maximum_subarray_sum(nums) == expected


# Test 2: all negative numbers
def test_maximum_subarray_all_negative():
    nums = [-8, -3, -6, -2, -5, -4]
    # Maximum subarray is just the least negative element: -2
    expected = -2
    assert maximum_subarray_sum(nums) == expected


# Test 1: basic knapsack example
def test_knapsack_basic():
    weights = [1, 2, 3]
    values = [6, 10, 12]
    cap = 5
    # Best choice: items with weight 2 and 3 --> value = 10 + 12 = 22
    expected = 22
    assert knapsack(cap, weights, values) == expected


# Test 2: capacity too small to take any item
def test_knapsack_no_fit():
    weights = [4, 5, 6]
    values = [10, 20, 30]
    cap = 3
    # No item fits, so result should be 0
    expected = 0
    assert knapsack(cap, weights, values) == expected


# Test 1: typical case with a 3x3 square of 1's inside -> area = 9
def test_largest_square_typical():
    matrix = [
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
    ]
    # The largest square of 1s has side length 3 -> area = 9
    expected = 9
    assert largest_square_in_a_matrix(matrix) == expected


# Test 2: no 1s in the matrix -> area = 0
def test_largest_square_all_zeros():
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
    ]
    expected = 0
    assert largest_square_in_a_matrix(matrix) == expected

