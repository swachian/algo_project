from collections import deque

class MultiLevelListNode:
    def __init__(self, val=None, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

def flatten_multi_level_list(head):
    cur = head
    childs = deque()
    while cur:
        if cur.child:
            childs.append(cur.child)
            cur.child = None
        if not cur.next and len(childs) > 0:
            child = childs.popleft()
            cur.next = child
        cur = cur.next
    return head