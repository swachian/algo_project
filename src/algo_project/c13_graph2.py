from collections import deque

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def shortest_transformation_sequence(start, end, dictionary):
    # 遍历各个位置上的26个字母的可能性，找出在dictionary且不在visited的中的单词，放入queue后继续遍历，直到遍历完或者找到end
    words = set(dictionary)
    if start not in words or end not in words:
        return 0
    visited = set()
    abc = "abcdefghijklmnopqrstuvwxyz"
    dist = 0
    queue = deque([start])
    
    while queue:
        level_size = len(queue)
        dist += 1
    
        for n in range(level_size):
            node = queue.popleft()
            if node == end:
                return dist
            for i in range(len(node)):
                for c in abc:
                    word = node[0:i] + c + node[i+1:]
                    if word not in visited and word in words:
                        queue.append(word)
            visited.add(node)
            
    return 0