from collections import deque

def shortest_transformation_sequence(start, end, words):
    if start not in words or end not in words:
        return 0
    
    abc = 'abcdefghijklmnopqrstuvwxyz'
    words_set = set(words)
    queue = deque()
    queue.append(start)
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
                    if new_word in words_set:
                        queue.append(new_word)
                        words_set.remove(new_word)
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
    graph = defaultdict(list)
    degrees = [0] * n
    enrolls = 0
    for a, b in prereqs:
        graph[a].append(b)
        degrees[b] += 1

    queue = deque()
    for i in range(n):
        if degrees[i] == 0:
            queue.append(i)
            enrolls += 1
    
    while queue and enrolls < n:
        a = queue.popleft()
        for neighbor in graph[a]:
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                enrolls += 1
                queue.append(neighbor)
    return enrolls == n
        

    
from collections import defaultdict
import heapq

def shortest_path(n, edges, start):
    graph = defaultdict(list)
    
    res = [float("inf")] * n

    for n1, n2, w in edges:
        graph[n1].append((w, n2))
        # graph[n2].append((w, n1))

    res[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        distance_all, node  = heapq.heappop(heap)
        for w, n2 in graph[node]:
            new_distance = distance_all + w
            if new_distance < res[n2]:
                heapq.heappush(heap, (new_distance, n2))
                res[n2] = new_distance
    
    return [ele if ele != float("inf") else -1 for ele in res]
            
   
import heapq 
def connect_the_dots(points):
    if not points:
        return 0
    heap = []
    n = len(points)
    uf = UnionFindDot(n)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            weight = abs(points[i][1] - points[j][1]) + abs(points[i][0] - points[j][0])
            heapq.heappush(heap, (weight, i, j))
    count = 1
    res = 0
    while heap and count < n:
        w, n1, n2 = heapq.heappop(heap)
        if uf.connect(n1, n2):
            res += w
            count += 1
    return res

class UnionFindDot:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.sizes = [1] * n
    
    def find(self, x):
        if self.parent[x] == x:
            return self.parent[x]
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connect(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x == rep_y:
            return False
        if self.sizes[rep_y] <= self.sizes[rep_x]:
            self.parent[rep_y] = rep_x
            self.sizes[rep_x] += self.sizes[rep_y]
        else:
            self.parent[rep_x] = rep_y
            self.sizes[rep_y] = self.sizes[rep_x]
            
        return True
        
    def get_size(self, x):
        return self.sizes[self.find(x)]
