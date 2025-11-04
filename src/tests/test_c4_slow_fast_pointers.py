import pytest
from algo_project.c4_slow_fast_pointers import ListNode, linked_list_loop, linked_list_midpoint, happy_number



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

def build_list(values):
    """Helper to build a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def test_midpoint_odd_length():
    """Should return the middle node for odd-length lists."""
    head = build_list([1, 2, 3, 4, 5])
    mid = linked_list_midpoint(head)
    assert mid.val == 3  # Middle of 5 elements


def test_midpoint_even_length():
    """Should return the second middle node for even-length lists."""
    head = build_list([1, 2, 3, 4, 5, 6])
    mid = linked_list_midpoint(head)
    assert mid.val == 4  # Second middle of 6 elements
    

def test_happy_number_true():
    """Should return True for a known happy number."""
    # 19 is a happy number because:
    # 1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1
    assert happy_number(19) is True


def test_happy_number_false():
    """Should return False for a number that ends in a cycle (unhappy number)."""
    # 4 is not a happy number — it falls into a loop:
    # 4² = 16 → 1² + 6² = 37 → 3² + 7² = 58 → 5² + 8² = 89 → 8² + 9² = 145 ...
    assert happy_number(4) is False
    
def test_happy_number_True4():
    """Should return False for a number that ends in a cycle (unhappy number)."""
    # 4 is not a happy number — it falls into a loop:
    # 4² = 16 → 1² + 6² = 37 → 3² + 7² = 58 → 5² + 8² = 89 → 8² + 9² = 145 ...
    assert happy_number(10) is True