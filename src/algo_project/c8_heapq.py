from collections import Counter
import heapq

class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq 
        
    def __lt__(self, y):
        if self.freq == y.freq:
            return self.word < y.word
        return self.freq > y.freq
    
    
def k_most_frequent_strings(strs, k):
    if  not strs:
        return []
    heap = []
    counters = Counter(strs)

    for str in counters.keys():
        pair = Pair(str, counters[str])
        heapq.heappush(heap, pair)
    return [heapq.heappop(heap).word for _ in range(k)]

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        

import heapq
        
def combine_sorted_linked_lists(lists):
    dummy = ListNode()
    cur = dummy
    
    ListNode.__lt__ = lambda x, y: x.val < y.val
    heap = []
    for head in lists:
        if head:
            heapq.heappush(heap, head)
    
    while heap:
        node = heapq.heappop(heap)
        cur.next = node
        if node.next:
            heapq.heappush(heap, node.next)
        cur = cur.next 
    return dummy.next


























def sort_a_k_sorted_array(nums, k):
    heap = []
    res = []
    for i, num in enumerate(nums):
        heapq.heappush(heap, num)
        if i >= k:
            res.append(heapq.heappop(heap))
    while heap:
        res.append(heapq.heappop(heap))
    return res