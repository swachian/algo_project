import pytest
from algo_project.c6_binary_search import find_the_insertion_index #, first_and_last_occurrences_of_a_number, cutting_wood, find_the_target_in_a_rotated_sorted_array
# from algo_project.c6_binary_search import find_the_median_from_two_sorted_arrays, matrix_search, local_maxima_in_array, WeightedRandomSelection



def test_find_insertion_index_existing_and_insert_middle():
    nums = [1, 3, 5, 6]
    assert find_the_insertion_index(nums, 3) == 1
    assert find_the_insertion_index(nums, 2) == 1
    assert find_the_insertion_index(nums, 7) == 4

def test_find_insertion_index_edge_cases():
    nums = [1, 3, 5, 6]
    assert find_the_insertion_index(nums, 0) == 0
    assert find_the_insertion_index([], 5) == 0
    assert find_the_insertion_index(nums, 6) == 3


# def test_basic_cases():
#     # Test when the target appears multiple times
#     # For nums = [1, 2, 2, 2, 3, 4], target = 2
#     # The first occurrence is at index 1, last at index 3
#     assert first_and_last_occurrences_of_a_number([1, 2, 2, 2, 3, 4], 2) == [1, 3]

#     # Test when the target appears only once
#     # nums = [1, 2, 3, 4, 5], target = 3 → [2, 2]
#     assert first_and_last_occurrences_of_a_number([1, 2, 3, 4, 5], 3) == [2, 2]


# def test_edge_cases():
#     # Target not found → return [-1, -1]
#     assert first_and_last_occurrences_of_a_number([1, 3, 5, 7], 2) == [-1, -1]

#     # Target is at the boundaries
#     # nums = [2, 2, 2, 3, 4], target = 2 → [0, 2]
#     assert first_and_last_occurrences_of_a_number([2, 2, 2, 3, 4], 2) == [0, 2]

#     # Empty array → no result
#     assert first_and_last_occurrences_of_a_number([], 5) == [-1, -1]
    
# def test_basic_cases_cutting_wood():
#     # Example: heights = [20, 15, 10, 17], k = 7
#     # If we set H = 15 → wood = (20-15) + (17-15) = 7
#     # That's exactly enough, and it's the highest possible height.
#     assert cutting_wood([20, 15, 10, 17], 7) == 15

#     # Example: heights = [4, 42, 40, 26, 46], k = 20
#     # The optimal H = 36 → wood = (42-36) + (40-36) + (46-36) = 20
#     assert cutting_wood([4, 42, 40, 26, 46], 20) == 36


# def test_edge_cases_cutting_wood():
#     # Case where no cutting is needed (k = 0)
#     # Any height up to tallest tree is valid, return tallest = 10
#     assert cutting_wood([5, 8, 10], 0) == 10

#     # Case where total wood cannot meet k (too large k)
#     # heights = [1, 2, 3], k = 10 → must cut at lowest possible (0)
#     # but even then total wood = 6 < 10 → still return 0
#     assert cutting_wood([1, 2, 3], 10) == 0
    
# def test_basic_cases_find_the_target_in_a_rotated_sorted_array():
#     # Example: nums = [4,5,6,7,0,1,2], target = 0 → index 4
#     # assert find_the_target_in_a_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4

#     # Example: nums = [4,5,6,7,0,1,2], target = 3 → not found → -1
#     # assert find_the_target_in_a_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3) == -1
    
#     assert find_the_target_in_a_rotated_sorted_array([4,5,6,7,0,1,2,3], 6) == 2
#     assert find_the_target_in_a_rotated_sorted_array([4,5,6,7,0,1,2,3], 3) == 7




# def test_edge_cases_find_the_target_in_a_rotated_sorted_array():
#     # Case: no rotation, regular sorted array
#     # nums = [1, 2, 3, 4, 5], target = 4 → index 3
#     assert find_the_target_in_a_rotated_sorted_array([1, 2, 3, 4, 5], 4) == 3

#     # Case: fully rotated (same as original), target not found
#     # nums = [1, 2, 3, 4, 5], target = 6 → -1
#     assert find_the_target_in_a_rotated_sorted_array([1, 2, 3, 4, 5], 6) == -1
    
    
# def test_basic_cases_find_the_median_from_two_sorted_arrays():
#     # Case 1: Even total length
#     # Merged array: [1, 2, 3, 4]
#     # Median = (2 + 3) / 2 = 2.5
#     assert find_the_median_from_two_sorted_arrays([1, 3], [2, 4]) == 2.5

#     # Case 2: Odd total length
#     # Merged array: [1, 2, 3]
#     # Median = 2
#     assert find_the_median_from_two_sorted_arrays([1, 2], [3]) == 2.0


# def test_edge_cases_find_the_median_from_two_sorted_arrays():
#     # One array empty
#     # nums1 = [], nums2 = [2, 3] → median = (2 + 3)/2 = 2.5
#     assert find_the_median_from_two_sorted_arrays([], [2, 3]) == 2.5

#     # Arrays with different sizes
#     # Merged array: [1, 2, 3, 4, 5]
#     # Median = 3
#     assert find_the_median_from_two_sorted_arrays([1, 2], [3, 4, 5]) == 3.0   
    
# def test_basic_cases_matrix_search():
#     # Matrix layout:
#     # [
#     #   [1, 3, 5],
#     #   [7, 9, 11],
#     #   [13, 15, 17]
#     # ]
#     matrix = [
#         [1, 3, 5],
#         [7, 9, 11],
#         [13, 15, 17]
#     ]
#     # Target 9 exists → True
#     assert matrix_search(matrix, 9) is True
#     # Target 6 not in matrix → False
#     assert matrix_search(matrix, 6) is False
    
#     matrix = [[2,3,4,6],[7,10,11,17],[20,21,24,33]]
#     assert matrix_search(matrix, 21) is True


# def test_edge_cases_matrix_search():
#     # Single row
#     matrix = [[2, 4, 6, 8]]
#     # Target 4 exists
#     assert matrix_search(matrix, 4) is True
#     # Target 5 does not exist
#     assert matrix_search(matrix, 5) is False

#     # Empty matrix
#     assert matrix_search([], 3) is False
    
# def test_basic_local_maxima_in_array():
#     # In [1, 3, 2, 5, 4], both 3 and 5 are local maxima — any one is valid.
#     result = local_maxima_in_array([1, 3, 2, 5, 4])
#     assert result in [3, 5]

# def test_edge_cases_local_maxima_in_array():
#     # Single-element array: that element is trivially a local maxima.
#     assert local_maxima_in_array([7]) == 7

#     # Strictly increasing array: last element is greater than out-of-bound neighbor.
#     assert local_maxima_in_array([1, 2, 3, 4]) == 4

#     # Strictly decreasing array: first element is greater than out-of-bound neighbor.
#     assert local_maxima_in_array([9, 7, 5, 3]) == 9
    
    
# def test_selection_probability_distribution():
#     # Test that items with larger weights are chosen more often statistically
#     weights = [3, 1, 2, 4]
#     selector = WeightedRandomSelection(weights)
#     counts = [0, 0, 0, 0]

#     # Run many selections to observe relative frequency
#     for _ in range(10000):
#         idx = selector.select()
#         counts[idx] += 1

#     # Expect index 3 (weight 4) to appear most, and index 1 (weight 1) least
#     assert counts[3] > counts[0] > counts[2] > counts[1]


# def test_single_weight_always_selected():
#     # When there is only one weight, it should always return index 0
#     selector = WeightedRandomSelection([10])
#     for _ in range(100):
#         assert selector.select() == 0