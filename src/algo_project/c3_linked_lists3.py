class MultiLevelListNode:
    def __init__(self, val=None, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child
 
from collections import deque
       
def flatten_multi_level_list(head):
    queue = deque()
    cur = head
    while cur:
        if cur.child:
            queue.append(cur.child)
            cur.child = None
        if not cur.next:
            if queue:
                node = queue.popleft()
                cur.next = node 
        cur = cur.next
    return head