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
            