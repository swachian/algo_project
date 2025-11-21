

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        
def graph_deep_copy(node):
    return dfs_graph(node)

def dfs_graph(node, visited = {}):
    if node in visited:
        return visited[node]
    new_node = GraphNode(node.val)
    visited[node] = new_node
    for neighbor in node.neighbors:
        new_node.neighbors.append(dfs_graph(neighbor))
    return new_node

def count_islands(matrix):
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    island_count = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                dfs_island(matrix, i, j)
                island_count += 1
    return island_count

def dfs_island(matrix, i, j):
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    matrix[i][j] = -1
    for dir in dirs:
        new_i = i + dir[0]
        new_j = j + dir[1]
        if is_valid_range(matrix, new_i, new_j) and matrix[new_i][new_j] == 1:
            dfs_island(matrix, new_i, new_j)
        
def is_valid_range(matrix, i, j):
    return i >= 0 and i < len(matrix) and j >=0 and j < len(matrix[0])

from collections import deque

def matrix_infection(matrix):
    queue = deque()
    ones_count = 0
    count = 0
    
    if not matrix:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 2:
                queue.append((i, j))
            if matrix[i][j] == 1:
                ones_count += 1
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]            
    while queue and ones_count > 0:
        level_size = len(queue)
        count += 1
        for c in range(level_size):
            node = queue.popleft()
            for dir in dirs:
                new_i, new_j = node[0] + dir[0], node[1] + dir[1]
                if is_i_j_inbount(new_i, new_j, m, n) and matrix[new_i][new_j] == 1:
                    matrix[new_i][new_j] = 2
                    ones_count -= 1
                    queue.append((new_i, new_j))
            
    return count if ones_count == 0 else -1
                
            
def is_i_j_inbount(i, j, m, n):
    return i >=0 and i < m and j >=0 and j < n

def bipartite_graph_validation(graph):
    colors = [0] * len(graph)
    for i in range(len(graph)):
        if colors[i] == 0 and not dfs_color_graph(i, 1, graph, colors):
            return False
    return True
        
def dfs_color_graph(node, color, graph, colors):
    colors[node] = color
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
        if colors[neighbor] == 0 and not dfs_color_graph(neighbor, -color, graph, colors):
            return False
    return True

def longest_increasing_path(matrix):
    if not matrix:
        return 0
    memo = [[0] * len(matrix[0]) for _ in range(len(matrix)) ]
    max_path = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            max_path = max(max_path, get_increasing_path(i, j, matrix, memo))
    return max_path
            
def get_increasing_path(i, j, matrix, memo):
    if memo[i][j] > 0:
        return memo[i][j]
    max_path = 1
    dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    for dir in dirs:
        n_i = i + dir[0]
        n_j = j + dir[1]
        if is_i_j_inbount(n_i, n_j, len(matrix), len(matrix[0])) and matrix[n_i][n_j] > matrix[i][j]:
            max_path = max(max_path, 1 + get_increasing_path(n_i, n_j, matrix, memo))
            
    memo[i][j] = max_path
    return max_path
    
def is_i_j_inbount(i, j, m, n):
    return i >=0 and i < m and j >=0 and j < n