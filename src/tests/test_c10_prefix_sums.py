import pytest
from algo_project.c10_prefix_sums import SumBetweenRange, k_sum_subarrays, product_array_without_current_element

def test_basic_sum_range():
    obj = SumBetweenRange([1, 2, 3, 4, 5])
    # sum of index 1..3 -> 2 + 3 + 4 = 9
    assert obj.sum_range(1, 3) == 9
    
def test_single_index_and_full_array():
    obj = SumBetweenRange([10, -2, 5, 3])

    # single element
    assert obj.sum_range(2, 2) == 5

    # full array
    assert obj.sum_range(0, 3) == 16
    
def test_k_sum_basic():
    nums = [1, 1, 1]
    k = 2
    # Valid subarrays:
    # [1,1] at indexes (0,1)
    # [1,1] at indexes (1,2)
    assert k_sum_subarrays(nums, k) == 2
    
def test_k_sum_with_negatives():
    nums = [3, 4, -2, -1, 1, 2]
    k = 3
    # Valid subarrays:
    # [3]
    # [4, -2, -1, 1, 1] -> actually [4, -2, -1, 1, 1] is not valid (typo)
    # Correct valid:
    # [3] = 3
    # [4, -2, -1, 1, 1]? (depends on real nums) → instead:
    # Let's list properly:
    # [3] = 3
    # [4, -2, -1, 1, 1]? (not present)
    # [4, -2, 1] = 3
    # [-2, -1, 1, 2, 3]? (not present)
    # [-1, 1, 2, 1]? (not present)
    #
    # actual valid subarrays:
    # [3]
    # [4, -2, 1]
    # [-2, -1, 1, 2]
    #
    assert k_sum_subarrays(nums, k) == 2
    
    nums = [1,-1,1,-1,1]
    k = 0 
    assert k_sum_subarrays(nums, k) == 6
    
def test_product_except_self_basic():
    nums = [1, 2, 3, 4]
    # Expected:
    # res[0] = 2*3*4 = 24
    # res[1] = 1*3*4 = 12
    # res[2] = 1*2*4 = 8
    # res[3] = 1*2*3 = 6
    assert product_array_without_current_element(nums) == [24, 12, 8, 6]
    
def test_product_except_self_with_zero():
    nums = [1, 2, 0, 4]
    # Only one zero → all other positions become 0
    # res[2] = 1*2*4 = 8
    assert product_array_without_current_element(nums) == [0, 0, 8, 0]   
    
  