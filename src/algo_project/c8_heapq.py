
from collections import Counter
import heapq


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Pair:
    def __init__(self, str, freq):
        self.str = str
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.str > other.str
        return self.freq < other.freq

def k_most_frequent_strings(strs, k):
    # 关键在于pair中的__lt__内置方法，heap按最小排序后，如果发现超出n,可以选择pop
    heap = []
    words_count = Counter(strs)
    
    for str, freq in words_count.items():
        pair = Pair(str, freq)
        heapq.heappush(heap, pair)
        if len(heap) > k:
            heapq.heappop(heap)
        
    result = [heapq.heappop(heap).str for _ in range(k) if len(heap) > 0]
    result.reverse()
    return result

def combine_sorted_linked_lists(lists):
    # 把几个list的头都塞进一个heap,然后找出其中最小的，如果最小的这个y有next,就再次塞入heap,直到heapw为空
    ListNode.__lt__ = lambda self, other: self.val < other.val
    
    dummy = ListNode()
    cur = dummy
    heap = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, node)
    
    while heap:
        cur.next = heapq.heappop(heap)
        cur = cur.next
        if cur.next:
            heapq.heappush(heap, cur.next)        
    return dummy.next

def sort_a_k_sorted_array(nums, k):
    # 利用最多离开k个位置，把前k个塞进一个heap后，每次从heap中选择最小的，然后再塞入。如果没有新的ele了，就可以连续弹出heap中的内容，完成排序
    result = []
    heap = []
    for i, num in enumerate(nums):
        if i <= k:
            heapq.heappush(heap, num)
        elif heap:
            min = heapq.heappop(heap)
            result.append(min)
            heapq.heappush(heap, num)
            
    while heap:
        result.append(heapq.heappop(heap))
        
    return result