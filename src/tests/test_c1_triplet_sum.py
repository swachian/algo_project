import pytest
from algo_project.c1_two_pointers import triplet_sum
from algo_project.c1_two_pointers import next_lexicographical_sequence, is_palindrome_valid, largest_container, shift_zeros_to_the_end

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

def test_largest_container():
    heights = [2, 7, 8, 3, 7, 6]
    result = largest_container(heights)
    assert  result == 24
    
def test_shift_zeros_to_the_end():
    nums = [0, 1, 0, 3, 2]
    result = shift_zeros_to_the_end(nums)
    assert result == [1, 3, 2, 0, 0]
    
def test_shift_zeros_to_the_end2():
    nums = [1, 2, 0, 0]
    result = shift_zeros_to_the_end(nums)
    assert result == [1, 2, 0, 0]
    
def test_next_lexicographical_sequence():
    s = 'abcedda'
    result = next_lexicographical_sequence(s)
    assert 'abdacde' == result
    
def test_next_lexicographical_sequence2():
    s = 'dcba'
    result = next_lexicographical_sequence(s)
    assert 'abcd' == result