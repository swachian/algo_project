
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