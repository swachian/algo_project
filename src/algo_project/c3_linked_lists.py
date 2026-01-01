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
    dummy = ListNode()
    dummy.next = head
    slow = fast = dummy
    while fast and k > 0:
        fast = fast.next
        k -= 1
    if k != 0:
        return dummy.next
    else:
        while fast.next:
            slow = slow.next 
            fast = fast.next 
        slow.next = slow.next.next 
    return dummy.next

        
def linked_list_intersection(head_A, head_B):
    p_a, p_b = head_A, head_B
    
    while p_a != p_b:
        p_a = p_a.next if p_a else head_B
        p_b = p_b.next if p_b else head_A
        
    return p_a


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
    slow = fast = dummy
    while fast.next and fast.next.next:
        slow = slow.next 
        fast = fast.next.next 
    mid = slow.next
    slow.next = None
    return mid 

def reverse_list(head):
    cur = head
    prev = None
    while cur:
        next_node = cur.next 
        cur.next = prev 
        prev = cur 
        cur = next_node
    return prev
    
    

