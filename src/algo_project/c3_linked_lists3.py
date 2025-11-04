from collections import deque

class MultiLevelListNode:
    def __init__(self, val=None, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

def flatten_multi_level_list(head):
    cur = head
    tail = get_cur_tail(cur)
    while cur:
        if cur.child:
            tail.next = cur.child
            cur.child = None
            tail = get_cur_tail(tail)
        cur = cur.next
    return head
    
    
def get_cur_tail(cur):
    while cur and cur.next:
        cur = cur.next
    return cur