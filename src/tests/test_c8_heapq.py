import pytest
from algo_project.c8_heapq import k_most_frequent_strings, ListNode, combine_sorted_linked_lists #, sort_a_k_sorted_array


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
    
def to_list(head):
    """Helper function to convert linked list to Python list."""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def test_basic_case_combine_sorted_linked_lists():
    # Input: [1 -> 4 -> 5], [1 -> 3 -> 4], [2 -> 6]
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    merged = combine_sorted_linked_lists([l1, l2, l3])
    # Expected merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
    assert to_list(merged) == [1, 1, 2, 3, 4, 4, 5, 6]

def test_with_empty_lists_combine_sorted_linked_lists():
    # Some lists are empty
    l1 = None
    l2 = ListNode(2, ListNode(3))
    l3 = None
    merged = combine_sorted_linked_lists([l1, l2, l3])
    # Expected: 2 -> 3
    assert to_list(merged) == [2, 3]
    
# def test_small_k_sorted_array():
#     """Test sorting with small k value."""
#     nums = [3, 2, 1, 5, 4, 6]
#     k = 2
#     result = sort_a_k_sorted_array(nums, k)
#     assert result == [1, 2, 3, 4, 5, 6]

# def test_already_sorted_array():
#     """Test when array is already sorted (k = 0)."""
#     nums = [1, 2, 3, 4, 5]
#     k = 0
#     result = sort_a_k_sorted_array(nums, k)
#     assert result == [1, 2, 3, 4, 5]