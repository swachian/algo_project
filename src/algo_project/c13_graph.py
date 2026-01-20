class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        
def graph_deep_copy(node):
    if not node:
        return node
    return dfs_graph_deep_copy(node)
    
def dfs_graph_deep_copy(node, memo = {}):
    if node in memo:
        return memo[node]
    new_node = GraphNode(node.val)
    memo[node] = new_node
    for neighbor in node.neighbors:
        new_node.neighbors.append(dfs_graph_deep_copy(neighbor, memo))
    return new_node


def count_islands(matrix):
    global count
    count = 0
    if not matrix:
        return count
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                dfs_count_islands(matrix, i, j)
                count += 1
    return count

def dfs_count_islands(matrix, i, j):
    matrix[i][j] = 0
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    for dir in dirs:
        new_i, new_j = i + dir[0], j + dir[1]
        if is_in_bound2(new_i, new_j, len(matrix), len(matrix[0])) and matrix[new_i][new_j] == 1:
            dfs_count_islands(matrix, new_i, new_j)
        
def is_in_bound2(i, j, m, n):
    return 0 <= i < m and 0 <= j < n

from collections import deque

def matrix_infection(matrix):
    if not matrix:
        return 0
    
    one_counts = 0
    infected = deque()
    second = 0
    
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 2:
                infected.append((i, j))
            elif matrix[i][j] == 1:
                one_counts += 1
    
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    while infected and one_counts > 0:
        second += 1
        level_size = len(infected)
        for _ in range(level_size):
            i, j = infected.popleft()
            for dir in dirs:
                n_i, n_j = i + dir[0], j + dir[1]
                if is_in_bound2(n_i, n_j, m, n) and matrix[n_i][n_j] == 1:
                    matrix[n_i][n_j] = 2
                    infected.append((n_i, n_j))
                    one_counts -= 1
    return second if one_counts == 0 else -1



def bipartite_graph_validation(graph):
    if not graph:
        return True
    colors = [0] * len(graph)
    for i in range(len(graph)):
        if colors[i] == 0 and not dfs_bipartitie_graph_validation(graph, i, 1, colors):
            return False
    return True

def dfs_bipartitie_graph_validation(graph, node, color, colors = []):
    colors[node] = color
    for neighor in graph[node]:
        if colors[neighor] == color:
            return False
        elif colors[neighor] == 0 and not dfs_bipartitie_graph_validation(graph, neighor, -color, colors):
            return False
    return True
            
def longest_increasing_path(matrix):
    if not matrix:
        return 0
    count = 0
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            count = max(count, dfs_longest_increasing_path(matrix, i, j, {}))
    return count

def dfs_longest_increasing_path(matrix, i, j, memo = {}):
    if (i, j) in memo:
        return memo[(i, j)]
    count = 1
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dir in dirs:
        n_i, n_j = i + dir[0], j + dir[1]
        if is_in_bound(n_i, n_j, len(matrix), len(matrix[0])) and matrix[n_i][n_j] > matrix[i][j]:
            count = max(count, 1 + dfs_longest_increasing_path(matrix, n_i, n_j, memo))
    memo[(i, j)] = count
    return count
        


                
def is_in_bound(i, j, m, n):
    return 0 <= i < m and 0 <= j < n