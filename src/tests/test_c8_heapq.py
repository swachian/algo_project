import pytest
from algo_project.c8_heapq import k_most_frequent_strings


def test_basic_case_k_most_frequent_strings():
    # 'apple' appears 3 times, 'banana' twice, 'cherry' once
    strings = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    k = 2
    # Expected: first by frequency desc → ['apple', 'banana']
    assert k_most_frequent_strings(strings, k) == ["apple", "banana"]

def test_tie_breaker_lexicographical_k_most_frequent_strings():
    # 'cat' and 'dog' appear 2 times each → tie → sort lexicographically
    strings = ["dog", "cat", "dog", "cat", "apple"]
    k = 2
    # Same frequency, so lexicographically 'cat' < 'dog'
    assert k_most_frequent_strings(strings, k) == ["cat", "dog"]

def test_empty_list_k_most_frequent_strings():
    assert k_most_frequent_strings([], 3) == []