class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None 

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.maps = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail 
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.maps:
            node = self.maps[key]
            node.prev.next = node.next 
            node.next.prev = node.prev
            
            self.tail.prev.next = node 
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            return node.val
        else:
            return -1
    
    def put(self, key, value):
        res = self.get(key)
        if res == -1 or res != value:
            node = Node(key, value)
            if key in self.maps:
                node = self.maps[key]
                node.val = value  
            self.maps[key] = node
            self.tail.prev.next = node 
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            if len(self.maps) > self.capacity:
                to_delete = self.head.next
                self.head.next.next.prev = self.head
                self.head.next = self.head.next.next 
                del self.maps[to_delete.key]
        

    
    
    
    
    