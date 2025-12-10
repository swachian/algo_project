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
    dummy = ListNode(None)
    dummy.next = head 
    slow = fast = dummy
    while fast.next and fast.next.next:
        slow = slow.next 
        fast = fast.next.next 
    return slow.next

def happy_number(n):
    slow = n 
    fast = get_squaring_sum(n)
    while fast != 1:
        if slow == fast:
            return False
        slow = get_squaring_sum(slow)
        fast = get_squaring_sum(get_squaring_sum(fast))
    return True

def get_squaring_sum(n):
    res = 0
    while n > 0:
        digit = n % 10
        res += digit * digit
        n = n // 10 
    return res