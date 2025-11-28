import pytest
from algo_project.c14_backtracking import find_all_permutations, find_all_subsets, n_queens

def test_find_all_permutations_empty_array():
    """Test that empty array returns list with empty permutation"""
    nums = []
    result = find_all_permutations(nums)
    
    # Empty array should return a list containing only an empty list
    assert result == [[]]
    
    # Should have exactly 1 permutation (0! = 1)
    assert len(result) == 1

def test_find_all_permutations_three_elements():
    """Test permutation generation for array with 3 unique elements"""
    nums = [1, 2, 3]
    result = find_all_permutations(nums)
    
    # For 3 elements, should have 3! = 6 permutations
    assert len(result) == 6
    
    # Check that all expected permutations are present
    expected_permutations = [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1], 
        [3, 1, 2], [3, 2, 1]
    ]
    
    # Convert both to sets of tuples for easy comparison
    result_set = {tuple(perm) for perm in result}
    expected_set = {tuple(perm) for perm in expected_permutations}
    
    assert result_set == expected_set
    
    # Verify no duplicates in result
    assert len(result) == len(set(tuple(perm) for perm in result))
    

# Assuming the function is imported from your module
# from your_module import find_all_subsets

def test_find_all_subsets_empty_array():
    """Test that empty array returns only the empty subset"""
    nums = []
    result = find_all_subsets(nums)
    
    # Empty array should return a list containing only an empty list
    expected = [[]]
    
    # Convert to sets of tuples for order-agnostic comparison
    result_set = {tuple(sorted(subset)) for subset in result}
    expected_set = {tuple(sorted(subset)) for subset in expected}
    
    assert result_set == expected_set
    assert len(result) == 1  # 2^0 = 1 subset

def test_find_all_subsets_three_elements():
    """Test subset generation for array with 3 unique elements"""
    nums = [1, 2, 3]
    result = find_all_subsets(nums)
    
    # For 3 elements, should have 2^3 = 8 subsets
    assert len(result) == 8
    
    # All expected subsets (order doesn't matter within subsets or in result list)
    expected_subsets = [
        [],
        [1], [2], [3],
        [1, 2], [1, 3], [2, 3],
        [1, 2, 3]
    ]
    
    # Convert both to sets of sorted tuples for comparison
    result_set = {tuple(sorted(subset)) for subset in result}
    expected_set = {tuple(sorted(subset)) for subset in expected_subsets}
    
    assert result_set == expected_set
    
    # Verify no duplicates in result
    assert len(result) == len(set(tuple(sorted(subset)) for subset in result))
    
import pytest

# Assuming the function is imported from your module
# from your_module import n_queens

def test_n_queens_small_boards():
    """Test n_queens with small board sizes where solutions are known"""
    # Known results for n = 1 to 8
    test_cases = [
        (1, 1),  # 1x1 board: 1 solution
        (2, 0),  # 2x2 board: 0 solutions
        (3, 0),  # 3x3 board: 0 solutions
        (4, 2),  # 4x4 board: 2 solutions
        (5, 10), # 5x5 board: 10 solutions
        (6, 4),  # 6x6 board: 4 solutions
    ]
    
    for n, expected in test_cases:
        result = n_queens(n)
        assert result == expected, f"Failed for n={n}: expected {expected}, got {result}"

def test_n_queens_known_sequence():
    """Test n_queens against known sequence values (OEIS A000170)"""
    # First few terms of the sequence for n-queens problem
    known_sequence = {
        1: 1,
        2: 0, 
        3: 0,
        4: 2,
        5: 10,
        6: 4,
        7: 40,
        8: 92,  # Classic 8-queens problem
    }
    
    for n, expected in known_sequence.items():
        # For larger n, we might want to skip due to computation time
        # But for testing, we can include them
        result = n_queens(n)
        assert result == expected, f"Failed for n={n}: expected {expected}, got {result}"