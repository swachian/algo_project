class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def sort_linked_list(head):
    # 1. split
    # 2. recurrenc 
    # 3. merge
    if not head or not head.next:
        return head
    head2 = split_linked_list(head)
    sorted1 = sort_linked_list(head)
    sorted2 = sort_linked_list(head2)

    return merge_linked_list(sorted1, sorted2)

def split_linked_list(head):

    dummy = ListNode()
    dummy.next = head
    slow, fast = dummy, dummy
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    res = slow.next
    slow.next = None
    return res
 
def merge_linked_list(h1, h2):
    dummy = ListNode()
    cur = dummy
    while h1 and h2:
        if h1.val <= h2.val:
            cur.next = h1 
            h1 = h1.next
        else:
            cur.next = h2
            h2 = h2.next 
        cur = cur.next
    if h1:
        cur.next = h1
    if h2:
        cur.next = h2
    return dummy.next
         
        
def sort_array(nums):
    if not nums:
        return nums
    # quick_sort(nums, 0, len(nums) - 1)
    res = merge_sort(nums)
    return res

def quick_sort(nums, i, j):
    if i > j:
        return
    pov = partition(nums, i, j)
    quick_sort(nums, i, pov - 1)
    quick_sort(nums, pov + 1, j)
    

def partition(nums, i, j):
    mid = i + (j - i) // 2
    nums[mid], nums[j] = nums[j], nums[mid]
    lo = 0
    scan = 0
    while scan < j - i:
        if nums[i + scan] <= nums[j]:
            nums[i + lo], nums[i + scan] = nums[i + scan], nums[i + lo]
            lo += 1
        scan += 1
    nums[i + lo], nums[j] = nums[j], nums[i + lo]
    return i + lo

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    left, right = 0, len(nums) - 1
    mid = left + (right - left) // 2
    sorted1 = merge_sort(nums[left:mid + 1])
    sorted2 = merge_sort(nums[mid + 1:])
    return merge_sorted(sorted1, sorted2)

def merge_sorted(nums1, nums2):
    res = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    while i < len(nums1):
        res.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        res.append(nums2[j])
        j += 1
    
    return res
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



import heapq
  
def kth_largest_integer(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def dutch_national_flag(nums):
    zero_p = 0
    two_p = len(nums) - 1
    one_p = 0
    while one_p <= two_p:
        if nums[one_p] == 0:
            nums[zero_p], nums[one_p] = nums[one_p], nums[zero_p]
            zero_p += 1
            one_p += 1
        elif nums[one_p] == 2:
            nums[two_p], nums[one_p] = nums[one_p], nums[two_p]
            two_p -= 1
        else:
            one_p += 1
        
    return nums
