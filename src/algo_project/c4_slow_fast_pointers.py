class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def linked_list_loop(head):
    slow, fast = head, head
    while slow or fast:
        slow = slow.next
        if fast:
            fast = fast.next
        if fast:
            fast = fast.next
        if slow == fast and slow:
            return True
    return False