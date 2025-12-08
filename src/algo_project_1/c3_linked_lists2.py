class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.value_map = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, key: int) -> int:
        if key not in self.value_map:
            return -1
        node = self.value_map[key]
        self.__remove_node__(node)
        self.__add_node__(node)
        return node.value
            

    def put(self, key: int, value: int) -> None:
        if len(self.value_map) >= self.capacity:
            del self.value_map[self.head.next.key]
            self.__remove_node__(self.head.next)
        node = Node(key, value)
        self.__add_node__(node)
        self.value_map[key] = node
        
    
    def __add_node__(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

        
        
    def __remove_node__(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    