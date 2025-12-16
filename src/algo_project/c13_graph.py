class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        
def graph_deep_copy(node):
    if not node:
        return node
    new_node = dfs_graph_deep_copy(node)
    return new_node

def dfs_graph_deep_copy(node, memo = {}):
    if node in memo:
        return memo[node]
    
    new_node = GraphNode(node.val)
    memo[node] = new_node
    for neighbor in node.neighbors:
        new_node.neighbors.append(dfs_graph_deep_copy(neighbor, memo))
    return new_node