import heapq

class MedianOfAnIntegerStream:
    # 此题核心是使用两个heap,左面放小的数字，右面放大的数字。但为了让左面最大的数字能在堆顶，所以
    # 需要按负数存入左堆，并且允许左堆最多可以比右堆多1个元素
    # 新元素到来时，如果小于左边，加负号后放入左面，否则放入右边; 然后检查左右堆是否平衡，不平衡就再次移动
    def __init__(self):
        self.max_left_heap = []
        self.min_right_heap = []
    
    def add(self, num):
        left_value = float("inf") if not self.max_left_heap else -self.max_left_heap[0]
        
        if num <= left_value:
            self.__add_left(num)
        else:
            self.__add_right(num)
            
        
        if len(self.max_left_heap) > len(self.min_right_heap) + 1:
            left_value = self.__pop_left()
            self.__add_right(left_value)
        
        if len(self.max_left_heap) < len(self.min_right_heap):
            self.__add_left(self.__pop_right())
            
    
    def get_median(self):
        if self.max_left_heap:
            if len(self.max_left_heap) == len(self.min_right_heap):
                return (-self.max_left_heap[0] + self.min_right_heap[0]) / 2
            else:
                return -self.max_left_heap[0]
        return None
    
    
    def __add_left(self, num):
        heapq.heappush(self.max_left_heap, -num)
        
    def __add_right(self, num):
        heapq.heappush(self.min_right_heap, num)
        
    def __pop_left(self):
        return -heapq.heappop(self.max_left_heap)
        
    def __pop_right(self):
        return heapq.heappop(self.min_right_heap)    