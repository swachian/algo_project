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
    
    return quick_sort(nums, 0, len(nums) - 1)
    # return merge_sort(nums)

def quick_sort(nums, left, right):
    if left >= right:
        return nums
    pov = quick_sort_partition(nums, left, right)
    quick_sort(nums, left, pov - 1)
    quick_sort(nums, pov + 1, right)
    return nums
    
def quick_sort_partition(nums, left, right):
    pov = left + (right - left) // 2
    # pov_value = nums[pov]
    nums[pov], nums[right] = nums[right], nums[pov]
    lo = 0
    for i in range(left, right):
        if nums[i] < nums[right]:
            nums[left + lo], nums[i] = nums[i], nums[left + lo]
            lo += 1
    nums[left + lo], nums[right] = nums[right], nums[left + lo]
    return left + lo
    
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    left, right = 0, len(nums) - 1
    if left < right:
        mid = left + (right - left) // 2
        sorted_nums1 = merge_sort(nums[left:mid + 1])
        sorted_nums2 = merge_sort(nums[mid + 1:])
        return merge_arr(sorted_nums1, sorted_nums2)

def merge_arr(nums1, nums2):
    res = []
    
    l1, l2 = 0, 0
    while l1 < len(nums1) and l2 < len(nums2):
        if nums1[l1] <= nums2[l2]:
            res.append(nums1[l1])
            l1 += 1
        else:
            res.append(nums2[l2])
            l2 += 1
    
    while l1 < len(nums1):
        res.append(nums1[l1])
        l1 += 1
        
    while l2 < len(nums2):
        res.append(nums2[l2])
        l2 += 1
        
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
