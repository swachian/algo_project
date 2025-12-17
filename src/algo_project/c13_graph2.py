from collections import deque

def shortest_transformation_sequence(start, end, words):
    words_set = set(words)
    visited = set()
    if start not in words_set or end not in words_set:
        return 0
    
    abc = "abcdefghijklmnopqrstuvwxyz"
    queue = deque()
    queue.append(start)
    visited.add(start)
    
    count = 0
    while queue:
        count += 1
        level_size = len(queue)
        for _ in range(level_size):
            word = queue.popleft()
            if word == end:
                return count
            for i in range(len(word)): 
                for c in abc:
                    new_word = word[0:i] + c + word[i + 1:]
                    if new_word in words_set and new_word not in visited:
                        queue.append(new_word)
                        visited.add(new_word)

                    
    return 0
    

class MergingCommunities:
    def __init__(self, n):
        self.uf = UnionFind(n)

    def connect(self, x, y):
        self.uf.connect(x, y)
    
    def get_community_size(self, x):
        return self.uf.get_size(x)
    
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.sizes = [1] * n
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def connect(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            if self.sizes[rep_x] >= self.sizes[rep_y]:
                self.parent[rep_y] = rep_x
                self.sizes[rep_x] += self.sizes[rep_y]
            else:
                self.parent[rep_x] = rep_y
                self.sizes[rep_y] += self.size[rep_x]
    
    def get_size(self, x):
        return self.sizes[self.find(x)]

from collections import defaultdict, deque

def prerequisites(n, prereqs):
    if not prereqs:
        return True
    
    graph = defaultdict(list)
    degrees = [0] * n
    enrolled = 0
    
    for a, b in prereqs:
        graph[a].append(b)
        degrees[b] += 1

    queue = deque()
    for i in range(n):
        if degrees[i] == 0:
            queue.append(i)
            enrolled += 1
            
    while queue and enrolled < n:
        node = queue.popleft()
        for neighbor in graph[node]:
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                queue.append(neighbor)
                enrolled += 1
    
    return enrolled == n
    
from collections import defaultdict, deque
import heapq

def shortest_path(n, edges, start):
    res = [float("inf")] * n
    
    graph = defaultdict(list)
    heap = []

    for s, e, weight in edges:
        graph[s].append((weight, e))
        # graph[e].append(weight, s)
    res[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        distance, start_node = heapq.heappop(heap)
        
        for weight, end_node in graph[start_node]:
            if distance + weight < res[end_node]:
                res[end_node] = distance + weight
                heapq.heappush(heap, (distance + weight, end_node))

    return [ele if ele != float("inf") else -1 for ele in res]
            
    
    
    
        