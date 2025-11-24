

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        
def graph_deep_copy(node):
    return dfs_clone_graph(node)

def dfs_clone_graph(node, node_map = {}):
    if node in node_map:
        return node_map[node]
    new_node = GraphNode(node.val)
    node_map[node] = new_node
    for neighbor in node.neighbors:
        new_node.neighbors.append(dfs_clone_graph(neighbor, node_map))
    return new_node
    

def count_islands(matrix):
    if not matrix:
        return 0
    island_count = 0
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                island_count += 1
                dfs_island(matrix, i, j, m, n)

    return island_count

def dfs_island(matrix, i, j, m, n):
    matrix[i][j] = 2
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dir in dirs:
        new_i, new_j = i + dir[0], j + dir[1]
        if is_i_j_inbount(new_i, new_j, m, n) and matrix[new_i][new_j] == 1:
            dfs_island(matrix, new_i, new_j, m, n)   
   

from collections import deque

def matrix_infection(matrix):
    queue = deque()
    ones_count = 0
    seconds = 0
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    
    if not matrix:
        return -1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                queue.append((i, j))
            elif matrix[i][j] == 1:
                ones_count += 1
    
    while queue and ones_count > 0:
        seconds += 1
        level_size = len(queue)
        for _ in range(level_size):
            i, j = queue.popleft()
            for dir in dirs:
                new_i, new_j = i + dir[0], j + dir[1]
                if is_i_j_inbount(new_i, new_j, len(matrix), len(matrix[0])) and matrix[new_i][new_j] == 1:
                    matrix[new_i][new_j] = 2
                    ones_count -= 1
                    queue.append((new_i, new_j))
        
    
    return seconds if ones_count == 0 else -1

            
def bipartite_graph_validation(graph):
    colors = [0] * len(graph)
    for i in range(len(graph)):
        if colors[i] == 0 and not dfs_color_traverse(graph, i, 1, colors):
            return False
    return True

def dfs_color_traverse(graph, node, color, colors):
    colors[node] = color
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
        elif colors[neighbor] == 0 and not dfs_color_traverse(graph, neighbor, -color, colors):
            return False
    return True

    


def longest_increasing_path(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0] * n for _ in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            count = max(count, dfs_sum_path(matrix, i, j, m, n, memo))
    return count
            
def dfs_sum_path(matrix, i, j, m, n, memo):
    if memo[i][j]:
        return memo[i][j]
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    count = 1
    for dir in dirs:
        new_i, new_j = i + dir[0], j + dir[1]
        if is_i_j_inbount(new_i, new_j, m, n) and matrix[new_i][new_j] > matrix[i][j]:
            count = max(count, 1 + dfs_sum_path(matrix, new_i, new_j, m, n, memo))
    memo[i][j] = count
    return count
    
    
def is_i_j_inbount(i, j, m, n):
    return i >=0 and i < m and j >=0 and j < n