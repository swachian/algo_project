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


def remove_kth_last_node(head, k):
    dummy = ListNode(None)
    dummy.next = head
    slow = fast = dummy
    for _ in range(k):
        fast = fast.next
        if not fast:
            return dummy.next
    while fast.next:
        fast = fast.next 
        slow = slow.next 
    slow.next = slow.next.next 
    return dummy.next

        
def linked_list_intersection(head_A, head_B):
    p_A, p_B = head_A, head_B
    
    while p_A != p_B:
        p_A = p_A.next if p_A else head_B
        p_B = p_B.next if p_B else head_A
    return p_A


def palindromic_linked_list(head):
    mid = find_middle(head)
    head2 = reverse_list(mid)
    
    while head and head2:
        if head.val != head2.val:
            return False
        head = head.next
        head2 = head2.next 
        
    return True

def find_middle(head):
    dummy = ListNode(None)
    dummy.next = head
    slow, fast = dummy, dummy
    
    while fast.next and fast.next.next:
        slow = slow.next 
        fast = fast.next.next 
    
    return slow.next 

def reverse_list(head):
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev 
        prev = cur
        cur = next_node
    return prev

    
    

