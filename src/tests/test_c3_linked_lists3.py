import pytest
from algo_project.c3_linked_lists3 import MultiLevelListNode, flatten_multi_level_list


def build_multi_level_list():
    """
    Helper function to build a multi-level linked list:
    1 - 2 - 3
        |
        4 - 5
    Expected flattened list: 1 - 2 - 4 - 5 - 3
    """
    node1 = MultiLevelListNode(1)
    node2 = MultiLevelListNode(2)
    node3 = MultiLevelListNode(3)
    node4 = MultiLevelListNode(4)
    node5 = MultiLevelListNode(5)

    node1.next = node2
    node2.next = node3
    node2.child = node4
    node4.next = node5

    return node1

def to_list(head):
    """Convert linked list to a Python list for easier comparison."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_flatten_empty_list():
    """Should return None for an empty list."""
    assert flatten_multi_level_list(None) is None


def test_flatten_single_level():
    """Should return the same list when there are no child nodes."""
    a = MultiLevelListNode(1)
    b = MultiLevelListNode(2)
    c = MultiLevelListNode(3)
    a.next, b.next = b, c

    head = flatten_multi_level_list(a)
    assert to_list(head) == [1, 2, 3]


def test_flatten_multi_level():
    """Should flatten multi-level structure correctly."""
    head = build_multi_level_list()
    flattened = flatten_multi_level_list(head)
    assert to_list(flattened) == [1, 2, 3, 4, 5]


def test_flatten_deep_child_chain():
    """
    Should handle deep nesting:
    1
    |
    2
    |
    3
    Expected flattened: 1 - 2 - 3
    """
    node1 = MultiLevelListNode(1)
    node2 = MultiLevelListNode(2)
    node3 = MultiLevelListNode(3)
    node1.child = node2
    node2.child = node3

    flattened = flatten_multi_level_list(node1)
    assert to_list(flattened) == [1, 2, 3]
