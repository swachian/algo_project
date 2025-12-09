class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None 

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.hash = {}
        self.head = Node(None, 'head')
        self.tail = Node(None, 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key not in self.hash:
            return -1
        node = self.hash[key]
        self.__remove_node(node)
        self.__add_head(node)
        return node.val
    
    def put(self, key, val):
        if len(self.hash) < self.capacity:
            node = Node(key, val)
            self.hash[key] = node
            self.__add_head(node)
        else:
            node = Node(key, val)
            self.hash[key] = node
            invalid_node = self.tail.prev 
            self.__remove_node(invalid_node)
            del self.hash[invalid_node.key] 
            self.__add_head(node)   
        
    def __add_head(self, node):   
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node    
    
    def __remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    
    
    
    
    