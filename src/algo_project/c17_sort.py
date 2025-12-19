class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def sort_linked_list(head):
    # 1. split
    # 2. recursplit and merge
    if not head or not head.next:
        return head
    head2 = split(head)
    sorted1 = sort_linked_list(head)
    sorted2 = sort_linked_list(head2)
    return merge_linked_list(sorted1, sorted2)

def split(head):
    slow = head 
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next 
        fast = fast.next.next 
        
    res = slow.next 
    slow.next = None
    return res

def merge_linked_list(head1, head2):
    dummy = ListNode(None)
    cur = dummy
    
    while head1 and head2:
        if head1.val <= head2.val:
            cur.next = head1 
            head1 = head1.next 
        else:
            cur.next = head2
            head2 = head2.next 
        cur = cur.next 
    
    cur.next = head1 or head2 
    return dummy.next    
        
def sort_array(nums):
    if not nums:
        return nums
    
    # quick_sort(nums, 0, len(nums) - 1)
    return merge_sort(nums)

def quick_sort(nums, left, right):
    if left >= right:
        return
    pov = split_quick(nums, left, right)
    quick_sort(nums, left, pov - 1)
    quick_sort(nums, pov + 1, right)
    
def split_quick(nums, left, right):
    pov = left + (right - left) // 2
    nums[pov], nums[right] = nums[right], nums[pov]
    
    i = lo = 0
    
    while i <= right - left:
        if nums[i + left] < nums[right]:
            nums[lo + left], nums[i + left] = nums[i + left], nums[lo + left] 
            lo += 1
        i += 1
    nums[lo + left], nums[right] = nums[right], nums[lo + left]
    return lo + left

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    pov = len(nums) // 2
    merged1 = merge_sort(nums[0:pov])
    merged2 = merge_sort(nums[pov:])

    return merge_array(merged1, merged2)
    
def merge_array(left, right):
    res = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    while i < len(left):
        res.append(left[i])
        i += 1
        
    while j < len(right):
        res.append(right[j])
        j += 1
        
    return res
  
import heapq
  
def kth_largest_integer(nums, k):
    if not nums:
        return None
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heapq.heappop(heap)

