class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
def linked_list_reversal(head):
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
        
    return prev
            