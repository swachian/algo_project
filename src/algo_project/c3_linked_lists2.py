class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.maps = {}
    
    def get(self, key):
        if key not in self.maps:
            return -1
        else:
            node = self.maps[key]
            self._remove_node(node)
            self._append_to_tail(node)
            return node.val
    
    def put(self, key, value):
        if key in self.maps:
            node = self.maps[key]
            node.val = value
            self._remove_node(node)
            self._append_to_tail(node)
        else:
            node = Node(key, value)
            self._append_to_tail(node)
            self.maps[key] = node
            if len(self.maps) > self.capacity:
                removing_node = self._remove_from_head()
                del self.maps[removing_node.key]
        
                
    
    def _append_to_tail(self, node):

        self.tail.prev.next = node 
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node 
        
    def _remove_from_head(self):
        if self.head.next.next != None:
            node = self.head.next
            next_node = self.head.next.next 
            self.head.next = next_node
            next_node.prev = self.head 
            return node
    
    def _remove_node(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev
        
        

    
    
    
    
    