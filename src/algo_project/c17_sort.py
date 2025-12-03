class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
def sort_linked_list(head):
    # 使用merge算法
    # merge的本质是先把集合打散成个体并返回head，然后再进行顺序的merge, 两个重要子方法是split和merge
    if not head or not head.next:
        return head
    second_head = split(head)
    sorted_head1 = sort_linked_list(head)
    sorted_head2 = sort_linked_list(second_head)
    
    return merge(sorted_head1, sorted_head2)
    
def split(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second_head = slow.next
    slow.next = None
    return second_head
            
def merge(head1, head2):
    dummy = ListNode(None)
    tail = dummy
    while head1 and head2:
        if head1.val <= head2.val:
            tail.next = head1
            tail = head1
            head1 = head1.next
        else:
            tail.next = head2
            tail = head2
            head2 = head2.next
    tail.next = head1 or head2
    return dummy.next