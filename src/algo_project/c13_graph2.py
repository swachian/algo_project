from collections import deque

def shortest_transformation_sequence(start, end, words):
    if start not in words or end not in words:
        return 0
    
    abc = "abcdefghijklmnopqrstuvwxyz"
    
    queue = deque()
    queue.append(start)
    visited = set()
    count = 0
    while queue:
        level_size = len(queue)
        count += 1
        for _ in range(level_size):
            
            word = queue.popleft()
            if word == end:
                return count
            for i in range(len(start)):
                for c in abc:
                    new_word = word[0:i] + c + word[i + 1:]
                    if new_word in words and new_word not in visited:
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
                self.sizes[rep_y] += self.sizes[rep_x]
    
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
    path_lengths = [float("inf")] * n
    
    heap = []
    graph = defaultdict(list)
    for n1, n2, w in edges:
        graph[n1].append((w, n2))
        # graph[n2].append((w, n1))
    
    path_lengths[start] = 0
    queue = deque()
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        distance = path_lengths[node]
        for w, n2 in graph[node]:
            heapq.heappush(heap, (w, n2))
        while heap:
            w, n2 = heapq.heappop(heap)
            if distance + w < path_lengths[n2]:
                path_lengths[n2] = distance + w
                queue.append(n2)
    return [ele if ele != float("inf") else -1 for ele in path_lengths]
    
    
            
   
import heapq 
def connect_the_dots(points):
    if not points:
        return 0
    edges = []
    n = len(points)
    for i in range(n):
        for j in range(n):
            edge_len = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            heapq.heappush(edges, (edge_len, i, j))
    uf = UFDot(n)
    edge_len, n1, n2 = heapq.heappop(edges)   
    node = n1
    total_len = edge_len
    uf.connect(n1, n2)     
    while edges:
        edge_len, n1, n2 = heapq.heappop(edges)
        if uf.connect(n1, n2):
            total_len += edge_len
            if uf.get_size(node) == n:
                break
    return total_len

class UFDot:
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
        if rep_x == rep_y:
            return False
        if self.sizes[rep_x] >= self.sizes[rep_y]:
            self.parent[rep_y] = rep_x
            self.sizes[rep_x] += self.sizes[rep_y]
        else:
            self.parent[rep_x] = rep_y
            self.sizes[rep_y] += self.sizes[rep_x]
        return True
        
    def get_size(self, x):
        return self.sizes[self.find(x)]