from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def invert_binary_tree(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return root

def balanced_binary_tree_validation(root):
    return get_height_of_tree(root) != -1
    
def get_height_of_tree(node):
    if not node:
        return 0
    left_depth = get_height_of_tree(node.left)
    right_depth = get_height_of_tree(node.right)
    if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
        return -1
    else:
        return 1 + max(left_depth, right_depth)


def rightmost_nodes_of_a_binary_tree(root):
    if not root:
        return []
    queue = deque()
    queue.append(root)
    
    result = []
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i == level_size - 1:
                result.append(node.val)
    return result

def widest_binary_tree_level(root):
    if not root:
        return 0
    
    queue = deque([(root, 0)])
    width = 0
    
    while queue:
        level_size = len(queue)
        left_most_index = queue[0][1]
        right_most_index = left_most_index
        for _ in range(level_size):
            node, index = queue.popleft()
            if node.left:
                queue.append((node.left, index * 2 + 1))
            if node.right:
                queue.append((node.right, index * 2 + 2))
            right_most_index = index
        width = max(width, right_most_index - left_most_index + 1)
    
    return width

def binary_search_tree_validation(root):
    if not root:
        return True
    return validate_binary_search_tree(root, float("-inf"), float("inf"))

def validate_binary_search_tree(node, lower_bound, upper_bound):
    if node.val <= lower_bound or node.val >= upper_bound:
        return False
    
    left_valid = validate_binary_search_tree(node.left, lower_bound, node.val) if node.left else True
    right_valid = validate_binary_search_tree(node.right, node.val, upper_bound) if node.right else True
        
    return left_valid and right_valid
    
def lowest_common_ancestor(root, p, q):
    dfs(root, p, q)
    return lca

def dfs(node, p, q):
    global lca
    
    if not node:
        return False
    node_is_p_or_q = node == p or node == q
    node_is_left = dfs(node.left, p, q)
    node_is_right = dfs(node.right, p, q)
    
    if (node_is_p_or_q + node_is_left + node_is_right) == 2:
        lca = node
        return True
    
    if node_is_p_or_q or node_is_left or node_is_right:
        return True
    else:
        return False
    


def build_binary_tree(preorder, inorder):
    global inorder_map
    global preorder_index
    inorder_map = {}
    preorder_index = 0
    for i in range(len(inorder)):
        inorder_map[inorder[i]] = i
        
    node = dfs_build(0, len(inorder) - 1, preorder, inorder)
    return node
    
def dfs_build(left, right, preorder, inorder):
    global inorder_map
    global preorder_index
    if left <= right:
        node = TreeNode(preorder[preorder_index])
        inorder_index = inorder_map[preorder[preorder_index]]
        preorder_index += 1
        node.left = dfs_build(left, inorder_index - 1, preorder, inorder)
        node.right = dfs_build(inorder_index + 1, right, preorder, inorder)
        return node
    else:
        return None
    
def max_path_sum(root):
    global max_sum
    max_sum = float("-inf")
    get_path_sum(root)
    return max_sum

def get_path_sum(node):
    global max_sum 
    if not node:
        return 0
    left_sum = max(get_path_sum(node.left), 0)
    right_sum = max(get_path_sum(node.right), 0)

    max_sum = max(max_sum, node.val + left_sum + right_sum) 
    return node.val + max(left_sum, right_sum) 

def binary_tree_symmetry(root):
    if not root:
        return True
    return compare_tree_symmetry(root.left, root.right)
    
def compare_tree_symmetry(node_left, node_right):
    if node_left and node_right:
        if node_left.val != node_right.val:
            return False
        return compare_tree_symmetry(node_left.left, node_right.right) and compare_tree_symmetry(node_left.right, node_right.left)
    elif not node_left and not node_right:
        return True
    else:
        return False
    
def binary_tree_columns(root):
    columns_map = defaultdict(list)
    
    if not root:
        return []
    left_most, right_most = 0, 0
    queque = deque([(root, 0)])
    while queque:
        node, column = queque.popleft()
        columns_map[column].append(node.val)
        if node.left:
            queque.append((node.left, column - 1))
            left_most = min(left_most, column - 1)
        if node.right:
            queque.append((node.right, column + 1))
            right_most = max(right_most, column + 1)
    
    return [columns_map[i] for i in range(left_most, right_most + 1)]

def kth_smallest_number_in_BST(root, k):
    # sorted_list = in_order_traverse(root, k)
    # return sorted_list[k - 1]
    return in_order_traverse(root, k)

# recursive 
def in_order_traverse2(node):
    if not node:
        return []
    result_left = in_order_traverse2(node.left)
    result = node.val
    result_right = in_order_traverse2(node.right)
    return result_left + [result] + result_right

# iterative
def in_order_traverse(root, k):
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
        
    return node.val