class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def invert_binary_tree(root):
    stack = []
    if not root:
        return 
    stack.append(root)
    
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return root

import math


def balanced_binary_tree_validation(root):
    if df_balanced_binary_tree_validation(root) > -1:
        return True
    return False

def df_balanced_binary_tree_validation(root):
    if not root:
        return 0
    
    left_height = df_balanced_binary_tree_validation(root.left) if root.left else 0
    right_height = df_balanced_binary_tree_validation(root.right) if root.right else 0
    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height + 1, right_height + 1)
                

from collections import deque

def rightmost_nodes_of_a_binary_tree(root):
    queue = deque()
    if not root:
        return []
    
    res = []
    queue.append(root)

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if i == level_size - 1:
                res.append(node.val)
    
    return res

def widest_binary_tree_level(root):
    queue = deque()
    
    if not root:
        return 0
    max_width = 0
    queue.append((0, root))
    while queue:
        level_size = len(queue)
        left = queue[0][0]
        for i in range(level_size):
            index, node = queue.popleft()
            if node.left:
                queue.append((2 * index + 1, node.left))
            if node.right:
                queue.append((2 * index + 2, node.right))
            max_width = max(max_width, index - left + 1)
    return max_width
            

    
def binary_search_tree_validation(root):
    return dfs_binary_search_tree_validation(root, float("-inf "), float("inf"))

def dfs_binary_search_tree_validation(root, low_bound, upper_bound):
    if not root:
        return True
    if low_bound < root.val < upper_bound:
        l = r = True
        if root.left:
            l = dfs_binary_search_tree_validation(root.left, low_bound, root.val)
        if root.right:
            r = dfs_binary_search_tree_validation(root.right, root.val, upper_bound)
        return l and r
    else:
        return False
    

