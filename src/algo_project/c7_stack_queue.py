class Queue:
    def __init__(self):
        self.left_stack = []
        self.right_stack = []
    
    def enqueue(self, x):
        self.left_stack.append(x)
    
    def dequeue(self):
        if self.right_stack:
            return self.right_stack.pop()
        elif self.left_stack:
            while self.left_stack:
                self.right_stack.append(self.left_stack.pop())
            return self.right_stack.pop()
        return None
    
    def peek(self):
        if self.right_stack:
            return self.right_stack[-1]
        elif self.left_stack:
            return self.left_stack[0]
        return None