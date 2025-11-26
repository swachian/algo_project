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

class UnionFind:
    # 1. 起初的parent就是自己
    # 2. 起初的size 都是1
    # 3. union方法，找到x,y的parent,根据大小把小的parent指向大的，并更新大的parent的size
    # 4. find找到parent,parent的特点是自己是自己的父亲，同时在递归查找的过程中更新self.parent[x]ww为root
    # 5. get size
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.sizes = [1] * n
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def get_size(self, i):
        parent = self.find(i)
        return self.sizes[parent]
    
    def union(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x == rep_y:
            return
        if self.sizes[rep_x] >= self.sizes[rep_y]:
            self.parent[rep_y] = rep_x
            self.sizes[rep_x] += self.sizes[rep_y]
        else:
            self.parent[rep_x] = rep_y
            self.sizes[rep_y] += self.sizes[rep_x]
            
        
    

class MergingCommunities:
    # 利用path compression,把子节点都指向根
    def __init__(self, n):
        self.union = UnionFind(n)
    
    def connect(self, x, y):
        self.union.union(x, y)
    
    def get_community_size(self, x):
        return self.union.get_size(x)