from collections import deque, defaultdict
import heapq

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
    
def prerequisites(n, prerequisites):
    # 构造邻接表的图和每个node对应的degrees数组
    # 把degree为0的node放入队列，并记录已经enroll
    # 从graph中读取依赖已经enroll的课程，并减1,如果该neighbor的degree为0,则也加入队列
    # 队列清空后，检查全部enroll的数量
    degrees = [0] * n
    graph = defaultdict(list)
    enrolls = 0
    
    for prereq, course in prerequisites:
        degrees[course] += 1
        graph[prereq].append(course)
    
    queue = deque()    
    for i in range(n):
        if degrees[i] == 0:
            queue.append(i)
            enrolls += 1
            
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                enrolls += 1
                queue.append(neighbor)
    return enrolls == n


def shortest_path(n, edges, start):
    # dijietesila算法
    # 构造邻接表的graph,构造表示每个点连接距离的数组，无向图的话每条边会影响两个邻接表节点，为inf代表不连通
    # 取出start,把对应的distance记录为0,将（距离，node）元记录在heap里
    # 每次从queue中取出当前最小的候选，如果候选的距离已经超过数组中的，则不再使用。否则把下一步可达节点的距离和node也写入heap中
    # 最后，把为inf状态的数组值改为-1
    graph = defaultdict(list)
    distances = [float("inf")] * n
    distances[start] = 0
    heap = []
    heapq.heappush(heap, (0, start)) 
    
    for node, node2, w in edges:
        graph[node].append((node2, w))
        # graph[node2].append(node, w)
        
    while heap:
        distance, current_node = heapq.heappop(heap)
        if distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))
    return [dist if dist != float("inf") else -1 for dist in distances ]
    
def connect_the_dots(points):
    # 1. 计算每条边之间的距离O(n2)
    # 2. 对edge进行排序
    # 3. 记录全edge长度的变量以及edge的数量
    # 4. 找出最短的边，并connect对应的两个点
    # 5. 找出剩余的最短的边，如果edge的节点已经连同，则放弃此边，寻找下一节点，并重复
    # 6. 边用光或者已加入的edge = node - 1
    edges = []
    for i in range(len(points)):
        for j in range(len(points)):
            edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
    edges.sort(key = lambda x: (x[0]))
    connected_edge_count = 0
    total_distance = 0
    
    uf = UnionFindForDots(len(points))
    
    for edge in edges:
        if connected_edge_count == len(points) - 1:
            break
        if uf.connect(edge[1], edge[2]):
            connected_edge_count += 1
            total_distance += edge[0]
    return total_distance    
    
class UnionFindForDots:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.sizes = [1] * n
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def connect(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x == rep_y:
            return False
        else:
            if self.sizes[rep_x] >= self.sizes[rep_y]:
                self.parent[rep_y] = self.parent[rep_x]
                self.sizes[rep_x] += self.sizes[rep_y]
            else:
                self.parent[rep_x] = self.parent[rep_y]
                self.sizes[rep_y] = self.parent[rep_x]
            return True