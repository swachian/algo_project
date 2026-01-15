import heapq

class MedianOfAnIntegerStream:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []
    
    def add(self, num):
        if not self.left_heap or -self.left_heap[0] >= num:
            heapq.heappush(self.left_heap, -num)
        else:
            heapq.heappush(self.right_heap, num)
        
        if len(self.left_heap) > len(self.right_heap) + 1:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        elif len(self.left_heap) < len(self.right_heap):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

    def get_median(self):
        if len(self.left_heap) == 0:
            return None
        
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0]) / 2 
        else:
            return -self.left_heap[0]