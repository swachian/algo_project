class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def invert_binary_tree(root):
    if not root:
        return root
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return root
    

import math


def balanced_binary_tree_validation(root):
    global is_balance 
    is_balance = True
    if not root:
        return True
    dfs_balanced_binary_tree_validation(root)
    return is_balance

def dfs_balanced_binary_tree_validation(root):
    global is_balance
    if not root:
        return 0
    left_depth = 1 + dfs_balanced_binary_tree_validation(root.left)
    right_depth = 1 + dfs_balanced_binary_tree_validation(root.right)
    if abs(left_depth - right_depth) >= 2:
        is_balance = False
    return max(left_depth, right_depth)

                

from collections import deque

def rightmost_nodes_of_a_binary_tree(root):
    res = []
    queue = deque()
    if not root:
        return res
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
    left = right = 0
    queue.append((root, 0))
    width = 0
    while queue:
        level_size = len(queue)
        left = queue[0][1]
        for _ in range(level_size):
            node, i = queue.popleft()
            right = i
            if node.left:
                queue.append((node.left, 2 * i))
            if node.right: 
                queue.append((node.right, 2 * i + 1))
        width = max(width, right - left + 1)
    return width


    
def binary_search_tree_validation(root):
    if not root:
        return True
    return dfs_binary_search_tree_validation(root, float("-inf"), float("inf"))

def dfs_binary_search_tree_validation(root, lower, upper):
    if not root:
        return True
    if lower < root.val < upper:
        return dfs_binary_search_tree_validation(root.left, lower, root.val) and dfs_binary_search_tree_validation(root.right, root.val, upper)
    else:
        return False
   
    
def lowest_common_ancestor(root, p, q):
    global lca
    lca = None
    dfs_lowest_common_ancestor(root, p, q)
    return lca

def dfs_lowest_common_ancestor(root, p, q):
    global lca
    p_or_q_is_node = 1 if root == p or root == q else 0
    p_or_q_is_in_left = dfs_lowest_common_ancestor(root.left, p, q) if root.left else 0
    p_or_q_is_in_right = dfs_lowest_common_ancestor(root.right, p, q) if root.right else 0
    if p_or_q_is_in_left + p_or_q_is_in_right + p_or_q_is_node == 2:
        lca = root
    return 1 if p_or_q_is_in_left + p_or_q_is_in_right + p_or_q_is_node >= 1 else 0
        

        
    
def build_binary_tree(preorder, inorder):
    global preorder_index
    global inorder_map
    preorder_index = 0
    inorder_map = {num: i for i, num in enumerate(inorder)}
    return dfs_build_binary_tree(preorder, inorder, 0, len(preorder) - 1)

def dfs_build_binary_tree(preorder, inorder, left, right):
    global preorder_index
    global inorder_map
    if left > right:
        return None
    val = preorder[preorder_index]
    preorder_index += 1
    pov = inorder_map[val]
    node = TreeNode(val)
    node.left = dfs_build_binary_tree(preorder, inorder, left, pov - 1)
    node.right = dfs_build_binary_tree(preorder, inorder, pov + 1, right)
    return node

def max_path_sum(root):
    global max_path_sum 
    max_path_sum = root.val
    dfs_max_path_sum(root)
    return max_path_sum

def dfs_max_path_sum(root):
    global max_path_sum 

    if not root:
        return 0
    
    left_value = max(0, dfs_max_path_sum(root.left))
    right_value = max(0, dfs_max_path_sum(root.right))
    max_path_sum = max(max_path_sum, root.val + left_value + right_value)
    return root.val + max(left_value, right_value)



def binary_tree_symmetry(root):
    if not root:
        return True
    return dfs_binary_tree_symmetry(root.left, root.right)

def dfs_binary_tree_symmetry(left, right):
    if not left and not right:
        return True
    elif not left and right:
        return False
    elif left and not right:
        return False
    else:
        if left.val != right.val:
            return False
        return dfs_binary_tree_symmetry(left.left, right.right) and dfs_binary_tree_symmetry(left.right, right.left)

from collections import defaultdict, deque

def binary_tree_columns(root):
    columns = defaultdict(list)
    queue = deque()
    res = []

    if not root:
        return res
    
    queue.append((root, 0))
    min_col = 0
    max_col = 0

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node, col = queue.popleft()
            columns[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
                min_col = min(min_col, col - 1)
            if node.right:
                queue.append((node.right, col + 1))
                max_col = max(max_col, col + 1)
    for i in range(min_col, max_col + 1):
        res.append(columns[i])
    
    return res
    



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
    stack = []
    if not root:
        return None
    count = 0
    cur = root
    res = []

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        count += 1
        res.append(cur.val)
        cur = cur.right
    return res[k - 1]    
   
    
END = "None"

def serialize(root):
    if not root:
        return END
    res = []
    dfs_serialize(root, res)
    return ",".join(res)

def dfs_serialize(node, res =[]):
    res.append(str(node.val))
    if node.left:
        dfs_serialize(node.left, res)
    else:
        res.append(END)
    if node.right:
        dfs_serialize(node.right, res)
    else:
        res.append(END)




def deserialize(data):
    if not data:
        return None
    data_list = iter(data.split(","))
    return dfs_deserialize(data_list)
    

def dfs_deserialize(data_list):
    data = next(data_list, None)
    if not data or data == END:
        return None
    node = TreeNode(int(data))
    node.left = dfs_deserialize(data_list)
    node.right = dfs_deserialize(data_list)
    return node
