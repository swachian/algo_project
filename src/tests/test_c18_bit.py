import pytest
from algo_project.c18_bit import hamming_weights_of_integers, lonely_integer, swap_odd_and_even_bits

import pytest

def test_hamming_weights_small_range():
    # For n = 5, binary representations:
    # 0 -> 0
    # 1 -> 1
    # 2 -> 10 -> 1
    # 3 -> 11 -> 2
    # 4 -> 100 -> 1
    # 5 -> 101 -> 2
    expected = [0, 1, 1, 2, 1, 2]
    assert hamming_weights_of_integers(5) == expected


def test_hamming_weights_zero():
    # Edge case: n = 0 → only one number (0), which has weight 0
    assert hamming_weights_of_integers(0) == [0]


import pytest

def test_lonely_integer_basic():
    # Basic case: the number 4 appears only once
    nums = [2, 3, 2, 4, 3]
    assert lonely_integer(nums) == 4


def test_lonely_integer_negative_numbers():
    # Works with negative integers as well
    nums = [-1, -2, -2, -3, -3]
    assert lonely_integer(nums) == -1

def test_swap_odd_and_even_bits_basic():
    # Example: n = 10 (binary 1010)
    # Swap adjacent bits: 10 10 -> 01 01 (binary) = 5
    assert swap_odd_and_even_bits(10) == 5


def test_swap_odd_and_even_bits_with_multiple_swaps():
    # n = 23 (binary 10111)
    # Pad to 8 bits: 00010111
    # Swapping pairs:
    # 00 01 01 11  -> 00 10 10 11 -> binary 00101011 = 43
    assert swap_odd_and_even_bits(23) == 43


