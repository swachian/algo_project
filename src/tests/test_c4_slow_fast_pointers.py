import pytest
from algo_project.c4_slow_fast_pointers import ListNode, linked_list_loop



def test_no_cycle():
    """Should return False when the linked list has no cycle."""
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    c.next = None

    assert linked_list_loop(a) is False


def test_with_cycle():
    """Should return True when a cycle exists in the linked list."""
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b  # creates a cycle (back to node b)

    assert linked_list_loop(a) is True
