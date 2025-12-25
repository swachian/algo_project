from collections import Counter
import heapq

class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    
def k_most_frequent_strings(strs, k):
    heap = []
    counters = Counter(strs)
    for word, freq in counters.items():
        pair = Pair(word, freq)
        heapq.heappush(heap, pair)
        if len(heap) > k:
            heapq.heappop(heap)

    results = [heapq.heappop(heap).word for _ in range(len(heap))]
    results.reverse()
    return results

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        

import heapq
        
def combine_sorted_linked_lists(lists):
    ListNode.__lt__ = lambda x, y: x.val < y.val 
    dummy = ListNode(None)
    cur = dummy
    
    heap = []

    for list_node in lists:
        if list_node:
            heapq.heappush(heap, list_node)
    
    while heap:
        node = heapq.heappop(heap)
        if node.next:
            heapq.heappush(heap, node.next)
        cur.next = node
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