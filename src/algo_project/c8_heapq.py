
from collections import Counter
import heapq


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
        
    result = [pair.str for pair in heap]
    result.reverse()
    return result