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
    
def lowest_common_ancestor(root, p, q):
    global res
    res = None
    dfs_lowest_common_ancestor(root, p, q)
    return res

def dfs_lowest_common_ancestor(node, p, q):
    global res
    
    if not node:
        return 0
    p_or_q_is_node = 1 if node == p or node == q else 0
    p_or_q_is_left = dfs_lowest_common_ancestor(node.left, p, q)
    p_or_q_is_right = dfs_lowest_common_ancestor(node.right, p, q)
    if p_or_q_is_right + p_or_q_is_left + p_or_q_is_node == 2 and not res:
        res = node

    return p_or_q_is_right + p_or_q_is_left + p_or_q_is_node
        
    
def build_binary_tree(preorder, inorder):
    global preorder_index
    preorder_index = 0
    pos_map = {}
    for i, num in enumerate(inorder):
        pos_map[num] = i
    root = dfs_build_binary_tree(preorder, inorder, 0, len(inorder) - 1, pos_map)
    return root
        

def dfs_build_binary_tree(preorder, inorder, left, right, pos_map):
    global preorder_index
    if left > right or preorder_index >= len(preorder):
        return None
    c = preorder[preorder_index]
    node = TreeNode(c)
    preorder_index += 1
    pov = pos_map[c]
    node.left = dfs_build_binary_tree(preorder, inorder, left, pov - 1, pos_map)
    node.right = dfs_build_binary_tree(preorder, inorder, pov + 1, right, pos_map)
    
    return node

def max_path_sum(root):
    global max_path
    max_path = root.val
    dfs_max_path_sum(root)
    return max_path

def dfs_max_path_sum(node):
    global max_path
    if not node:
        return 0
    
    left_depth = max(0, dfs_max_path_sum(node.left))
    right_depth = max(0, dfs_max_path_sum(node.right))
    max_path = max(max_path, left_depth + node.val + right_depth)
    return max(left_depth, right_depth) + node.val

def binary_tree_symmetry(root):
    if not root:
        return True
    return dfs_binary_tree_symmetry(root.left, root.right)

def dfs_binary_tree_symmetry(left, right):
    if not left and not right:
        return True
    if not left and right:
        return False
    if left and not right:
        return False
    if left.val != right.val:
        return False
    return dfs_binary_tree_symmetry(left.left, right.right) and dfs_binary_tree_symmetry(left.right, right.left) 

from collections import defaultdict, deque

def binary_tree_columns(root):
    queue = deque()
    if not root:
        return []
    
    res = defaultdict(list)    
    queue.append((root, 0))
    i = j = 0
    while queue:
        node, index = queue.popleft()
        res[index].append(node.val)
        i = min(i, index)
        j = max(j, index)
        if node.left:
            queue.append((node.left, index - 1))
        if node.right:
            queue.append((node.right, index + 1))
    
    return [res[k] for k in range(i, j + 1)]

def kth_smallest_number_in_BST(root, k):
    return kth_smallest_number_in_BST_stack_version(root, k)
    # res = []
    # dfs_kth_smallest_number_in_BST(root, res)
    # return res[k - 1]

def dfs_kth_smallest_number_in_BST(node, res):
    if not node:
        return
    
    dfs_kth_smallest_number_in_BST(node.left, res)
    res.append(node.val)
    dfs_kth_smallest_number_in_BST(node.right, res)
    
def kth_smallest_number_in_BST_stack_version(root, k):
    if not root:
        return None
    
    stack = []
    node = root
    
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    return None
    
END = "None"

def serialize(root):
    global res
    res = []
    dfs_serialize(root)
    return ','.join([str(ele) for ele in res])

def dfs_serialize(node):
    global res
    if not node:
        res.append(END) 
        return
    res.append(node.val)
    dfs_serialize(node.left) 
    dfs_serialize(node.right) 


def deserialize(data):
    global index
    index = 0
    lists = data.split(",")
    return dfs_deserialize(lists)

def dfs_deserialize(data):
    global index
    if index >= len(data) or data[index] == END:
        index += 1
        return None
    node = TreeNode(int(data[index]))
    index += 1
    node.left = dfs_deserialize(data)
    node.right = dfs_deserialize(data)
    return node
    