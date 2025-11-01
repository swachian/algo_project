import pytest
from algo_project.c3_linked_lists import linked_list_reversal, ListNode


def build_linked_list(values):
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head


# Helper: convert a linked list back to a Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_empty_list():
    """Reversing an empty list should return None."""
    head = None
    assert linked_list_reversal(head) is None


def test_single_node():
    """Reversing a single-node list should return the same node."""
    head = ListNode(1)
    result = linked_list_reversal(head)
    assert linked_list_to_list(result) == [1]


def test_two_nodes():
    """Reversing two nodes should swap their order."""
    head = build_linked_list([1, 2])
    result = linked_list_reversal(head)
    assert linked_list_to_list(result) == [2, 1]


def test_multiple_nodes():
    """Reversing multiple nodes should fully invert their order."""
    head = build_linked_list([1, 2, 3, 4, 5])
    result = linked_list_reversal(head)
    assert linked_list_to_list(result) == [5, 4, 3, 2, 1]


def test_reverse_twice_returns_original():
    """Reversing a list twice should yield the original order."""
    original = [10, 20, 30]
    head = build_linked_list(original)
    reversed_once = linked_list_reversal(head)
    reversed_twice = linked_list_reversal(reversed_once)
    assert linked_list_to_list(reversed_twice) == original