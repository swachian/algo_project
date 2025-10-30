import pytest
from algo_project.c1_two_pointers import triplet_sum
from algo_project.c1_two_pointers import is_palindrome_valid

def test_triplet_sum1():
    nums = [0, -1, 2, -3, 1]
    result = triplet_sum(nums)
    assert sorted(result) == [[-3, 1, 2], [-1, 0, 1]]
    
def test_is_palindrome_valid():
    s = 'a dog! a panic in a pagoda.'
    result = is_palindrome_valid(s)
    assert(result)

def test_is_palindrome_valid_false():
    s = 'abc123'
    result = is_palindrome_valid(s)
    assert(result == False)
