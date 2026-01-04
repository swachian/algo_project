class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
def linked_list_loop(head):
    slow, fast = head, head
    while fast and fast.next:

        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True
    return False
         


def linked_list_midpoint(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
    return slow


def happy_number(n):
    slow = n
    fast = compute_happy_num(n)
    while True:
        if slow == 1:
            return True
        if slow == fast:
            return False
        slow = compute_happy_num(slow)
        fast = compute_happy_num(compute_happy_num(fast))

def compute_happy_num(n):
    res = 0
    while n > 0:
        d = n % 10
        res += d * d
        n //= 10
    return res
    
