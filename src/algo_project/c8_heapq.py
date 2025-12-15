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
        

        
def combine_sorted_linked_lists(lists):
    ListNode.__lt__ = lambda self, other: self.val < other.val
    heap = []
    head = None
    cur = head
    for list in lists:
        if list:
            heapq.heappush(heap, list)
            
    while heap:
        if not head:
            head = heapq.heappop(heap)
            cur = head
        else:
            node = heapq.heappop(heap)
            cur.next = node
            cur = node
        if cur.next:
            heapq.heappush(heap, cur.next)
    return head

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