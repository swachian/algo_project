class Queue:
    # 用两个栈模拟，一个入栈in,一个出栈out,增加元素时，都加入in栈，当取出元素时，直接从out栈pop,如果out
    # 为空，则把in的都pop然后push进去。peek也是更加in和out的空的情况取不同的元素
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    def enqueue(self, x):
        self.in_stack.append(x)
        
    
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack.pop() if self.out_stack else None
                
    
    def peek(self):
        if self.out_stack:
            return self.out_stack[-1]
        elif self.in_stack:
            return self.in_stack[0]
        else:
            return None