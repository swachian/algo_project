import pytest
from algo_project.c17_sort import ListNode, sort_linked_list




def to_list(head):
    """Convert linked list to Python list for easy comparison."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def from_list(values):
    """Convert Python list to linked list."""
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def test_sort_linked_list_basic():
    # Basic unsorted list
    head = from_list([4, 2, 1, 3])
    sorted_head = sort_linked_list(head)

    # Expected sorted list
    assert to_list(sorted_head) == [1, 2, 3, 4]


def test_sort_linked_list_with_duplicates():
    # List containing duplicates
    head = from_list([5, 3, 3, 2, 4])
    sorted_head = sort_linked_list(head)

    # Expected sorted list
    assert to_list(sorted_head) == [2, 3, 3, 4, 5]
