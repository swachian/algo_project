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

def sort_array(nums):
    # 0 1 2 ^ 3 4, 从中间劈开来后，左面的一起，右面的一起，直到分到每边只有一个元素才返回继续merge
    r = len(nums) - 1
    merge_helper(nums, 0, r)
    return nums

def merge_helper(nums, l, r):
    if l < r:
        pivot = l + (r - l) // 2
        merge_helper(nums, l, pivot)
        merge_helper(nums, pivot + 1, r)
        merge2(nums, l, pivot, r)
    
def merge2(nums, l, pivot, r):
    m = pivot - l + 1
    n = r - pivot
    L1 = nums[l:pivot + 1]
    L2 = nums[pivot + 1:r + 1]    
    
    i, j = 0, 0
    k = l
    while i < m and j < n:
        if L1[i] <= L2[j]:
            nums[k] = L1[i]
            i += 1
        else:
            nums[k] = L2[j]
            j += 1
        k += 1
        
    while i < m:
        nums[k] = L1[i]
        i += 1
        k += 1
        
    while j < n:
        nums[k] = L2[j]
        j += 1
        k += 1
        
def quik_sort(nums, l, r):
    if l < r:
        pivot = partition(nums, l, r)
        
        quik_sort(nums, l, pivot - 1)
        quik_sort(nums, pivot + 1, r)

def partition(nums, l, r):
    pivot_value = nums[r]
    lo = 0
    for i in range(r - l):
        if nums[i + l] < pivot_value:
            nums[i + l], nums[lo + l] = nums[lo + l], nums[i + l]
            lo += 1
    nums[lo + l], nums[r] = nums[r], nums[lo + l]
    return lo + l        
        
import heapq

def kth_largest_integer(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
    return heapq.heappop(heap)