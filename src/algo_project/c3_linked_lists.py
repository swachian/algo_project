class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
def linked_list_reversal(head):
    if not head or not head.next:
        return head
    new_head = linked_list_reversal(head.next)
    head.next.next = head
    head.next = None
    return new_head
            
def remove_kth_last_node(head, k):
    slow, fast = head, head
    for _ in range(k):
        if not fast:
            return head
        fast = fast.next
    if not fast:
        slow = head.next
        head.next = None
        return slow
    while fast.next:
        slow = slow.next
        fast = fast.next 
    slow.next = slow.next.next
    return head