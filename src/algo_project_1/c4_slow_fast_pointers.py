class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def linked_list_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def linked_list_midpoint(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
    return slow

def happy_number(n):
    slow, fast = n, n
    while True:
        slow = get_next_number(slow)
        fast = get_next_number(get_next_number(fast))
        if fast == 1:
            return True
        elif fast == slow:
            return False

def get_next_number(n):
    sum = 0
    while n > 0:
        d = n % 10
        sum += d * d
        n = n // 10
    return sum