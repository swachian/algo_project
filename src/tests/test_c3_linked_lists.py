import pytest
from algo_project.c3_linked_lists import linked_list_reversal, ListNode, remove_kth_last_node, linked_list_intersection


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

def get_tail(head):
    """Returns the last node of a linked list."""
    while head and head.next:
        head = head.next
    return head

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
    
    
    
def test_remove_from_middle():
    """Remove the 2nd last node from [1, 2, 3, 4, 5] -> should remove 4."""
    head = build_linked_list([1, 2, 3, 4, 5])
    result = remove_kth_last_node(head, 2)
    assert linked_list_to_list(result) == [1, 2, 3, 5]


def test_remove_last_node():
    """Remove the last node (k=1) from [1, 2, 3] -> should remove 3."""
    head = build_linked_list([1, 2, 3])
    result = remove_kth_last_node(head, 1)
    assert linked_list_to_list(result) == [1, 2]


def test_remove_head_node():
    """Remove the 3rd last node (head) from [1, 2, 3] -> should remove 1."""
    head = build_linked_list([1, 2, 3])
    result = remove_kth_last_node(head, 3)
    assert linked_list_to_list(result) == [2, 3]


def test_single_node():
    """Remove the only node from [1] -> should return None."""
    head = build_linked_list([1])
    result = remove_kth_last_node(head, 1)
    assert result is None


def test_k_equals_list_length():
    """When k equals the list length, remove the first node."""
    head = build_linked_list([10, 20, 30, 40])
    result = remove_kth_last_node(head, 4)
    assert linked_list_to_list(result) == [20, 30, 40]
    
def test_intersection_in_middle():
    """Two lists intersect at a middle node."""
    # Common part: [8, 9]
    common = build_linked_list([8, 9])
    # List A: [1, 2, 3] + [8, 9]
    head_A = build_linked_list([1, 2, 3])
    get_tail(head_A).next = common
    # List B: [4, 5] + [8, 9]
    head_B = build_linked_list([4, 5])
    get_tail(head_B).next = common

    result = linked_list_intersection(head_A, head_B)
    assert result == common, "Should return the first intersecting node"
    assert result.val == 8
