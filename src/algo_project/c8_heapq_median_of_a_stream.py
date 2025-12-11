import heapq

class MedianOfAnIntegerStream:
    def __init__(self):
        self.left_heap = []
        self.right_heap =[]

    def add(self, num: int) -> None:
        if not self.left_heap:
            heapq.heappush(self.left_heap, -num)
            return 
        if -self.left_heap[0] > num:
            heapq.heappush(self.left_heap, -num)
        else: 
            heapq.heappush(self.right_heap, num)
            
        if len(self.left_heap) > len(self.right_heap) + 1:
            ele = -heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, ele)
        
        if len(self.right_heap) > len(self.left_heap):
            ele = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -ele)
            

    def get_median(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0]) / 2
        else:
            return -self.left_heap[0]