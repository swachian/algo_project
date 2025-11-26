

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        
def graph_deep_copy(node):
    if not node:
        return None
    return dfs_graph_deep_copy(node)

def dfs_graph_deep_copy(node, nodes_map = {}):
    if node in nodes_map:
        return nodes_map[node]
    new_node = GraphNode(node.val)
    nodes_map[node] = new_node 
    for neighbor in node.neighbors:
        new_node.neighbors.append(dfs_graph_deep_copy(neighbor))
    return new_node
    

def count_islands(matrix):
    if not matrix:
        return 0
    island_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                dfs_count_islands(matrix, i, j)
                island_count += 1
    return island_count

def dfs_count_islands(matrix, i, j):
    matrix[i][j] = 0
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dir in dirs:
        new_i, new_j = i + dir[0], j + dir[1]
        if is_i_j_inbount(new_i, new_j, len(matrix), len(matrix[0])) and matrix[new_i][new_j] == 1:
            dfs_count_islands(matrix, new_i, new_j)

   

from collections import deque




def matrix_infection(matrix):
    if not matrix:
        return 0
    seconds = 0
    ones = 0
    queue = deque()
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                queue.append((i, j))
            elif matrix[i][j] == 1:
                ones += 1
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while queue and ones > 0:
        level_size = len(queue)
        seconds += 1
        for _ in range(level_size):
            i, j = queue.popleft()
            for dir in dirs:
                new_i, new_j = i + dir[0], j + dir[1]
                if is_i_j_inbount(new_i, new_j, len(matrix), len(matrix[0])) and matrix[new_i][new_j] == 1:
                    matrix[new_i][new_j] = 2
                    queue.append((new_i, new_j))    
                    ones -= 1

    return seconds if ones == 0 else -1 
        
 

            
def bipartite_graph_validation(graph):
    if not graph:
        return True
    colors_map = [0] * len(graph)
    for i in range(len(graph)):
        if colors_map[i] == 0 and not dfs_bipartite_graph_validation(graph, i, 1, colors_map):
            return False
    return True
    
def dfs_bipartite_graph_validation(graph, i, color, colors_map):
    colors_map[i] = color
    for neighbor in graph[i]:
        if colors_map[neighbor] == color:
            return False
        if colors_map[neighbor] == 0 and not dfs_bipartite_graph_validation(graph, neighbor, -color, colors_map):
            return False
    return True 

    


def longest_increasing_path(matrix):
    max_path = 0
    if not matrix:
        return 0
    memo = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            max_path = max(max_path, dfs_longest_increasing_path(matrix, i, j, memo))
    return max_path
            
def dfs_longest_increasing_path(matrix, i, j, memo):
    if memo[i][j] != 0:
        return memo[i][j]
    path_sum = 1
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    cur_sum = 0
    
    for dir in dirs:
        new_i, new_j = i + dir[0], j + dir[1]
        if is_i_j_inbount(new_i, new_j, len(matrix), len(matrix[0])) and matrix[new_i][new_j] > matrix[i][j]:
            cur_sum = max(cur_sum, dfs_longest_increasing_path(matrix, new_i, new_j, memo))
    path_sum = path_sum + cur_sum
    memo[i][j] = path_sum
    return path_sum
    
def is_i_j_inbount(i, j, m, n):
    return i >=0 and i < m and j >=0 and j < n