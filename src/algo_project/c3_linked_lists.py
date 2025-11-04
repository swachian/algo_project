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
    dummy = ListNode(-1)
    dummy.next = head
    slow = fast = dummy
    for _ in range(k):
        if not fast:
            return head
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next 
    slow.next = slow.next.next
    return dummy.next

def linked_list_intersection(head_A, head_B):
    p_A = head_A
    p_B = head_B
    a_passed = False
    b_passed = False
    while p_A and p_B:
        if p_A == p_B:
            return p_A
        p_A = p_A.next
        p_B = p_B.next
        if not a_passed and not p_A:
            p_A = head_B
            a_passed = True
        if not b_passed and not p_B:
            p_B = head_A
            b_passed = True
    return None
        

def palindromic_linked_list(head):
    mid = __find_mid_linked_list__(head)
    reserved2 = __rervese_linked_list__(mid)
    p1, p2 = head, reserved2
    while p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True
        

def __rervese_linked_list__(head):
    prev, cur = None, head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev

def __find_mid_linked_list__(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow
        
        