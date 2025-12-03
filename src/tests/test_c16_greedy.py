import pytest
from algo_project.c16_greedy import jump_to_the_end, gas_stations, candies


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

import pytest

# Test 1: typical valid case
def test_gas_stations_valid():
    gas =  [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    # Explanation:
    # Start at index 3:
    #   gas left after 3→4: 4-1 = 3
    #   3 + 5 - 2 = 6
    #   6 + 1 - 3 = 4
    #   4 + 2 - 4 = 2
    #   2 + 3 - 5 = 0  (back to start)
    expected = 3
    assert gas_stations(gas, cost) == expected


# Test 2: impossible case
def test_gas_stations_impossible():
    gas =  [2, 3, 4]
    cost = [3, 4, 3]
    # Total gas < total cost → impossible
    expected = -1
    assert gas_stations(gas, cost) == expected

def test_candies_strictly_increasing():
    # Ratings strictly increasing
    # Expected candy distribution: 1, 2, 3 → total = 6
    ratings = [1, 2, 3]
    assert candies(ratings) == 6


def test_candies_peak_and_valley():
    # Mixed ratings with a peak and a valley
    # Expected candy distribution: 1, 2, 3, 4, 1 → total = 11
    ratings = [1, 3, 4, 5, 2]
    assert candies(ratings) == 11
