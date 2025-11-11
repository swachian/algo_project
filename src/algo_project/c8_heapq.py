import heapq
from collections import Counter

class Pair:
    def __init__(self, str, freq):
        self.str = str
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.str < other.str
        return self.freq > other.freq
        
        
        
def k_most_frequent_strings(strs, k):
    words_count = Counter(strs)
    heap = []
    for str, freq in words_count.items():
        pair = Pair(str, freq)
        heapq.heappush(heap, pair)
        
    result = [heapq.heappop(heap).str for _ in range(k) if len(heap) > 0 ]
    return result