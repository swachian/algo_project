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
                