from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
()
#        
def invert_binary_tree(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return root
        

#
def balanced_binary_tree_validation(root):
    return get_balanced_tree(root) != -1

def get_balanced_tree(node, height = 0):
    if not node:
        return height
    left_depth = get_balanced_tree(node.left, height + 1)
    right_depth = get_balanced_tree(node.right, height + 1)
    if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
        return -1
    return max(left_depth, right_depth)


#
def rightmost_nodes_of_a_binary_tree(root):
    if not root:
        return []
    queue = deque()
    result = []
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
                result.append(node.val)
    return result

#
def widest_binary_tree_level(root):
    if not root:
        return 0
    queue = deque()
    queue.append((root, 0))
    span = 0
    
    while queue:
        level_size = len(queue)
        left_most = queue[0][1]
        right_most = left_most
        for i in range(level_size):
            node, i = queue.popleft()
            right_most = i
            if node.left:
                queue.append((node.left, i * 2))
            if node.right:
                queue.append((node.right, i * 2 + 1))
        span = max(span, right_most - left_most + 1)
    return span          

#
def binary_search_tree_validation(root):
    return validate_bst(root, float("-inf"), float("inf"))

def validate_bst(node, lower_bound, upper_bound):
    if not node:
        return True
    if node.val > lower_bound and node.val < upper_bound:
        return validate_bst(node.left, lower_bound, node.val) and validate_bst(node.right, node.val, upper_bound)
    else:
        return False

    
def lowest_common_ancestor(root, p, q):
    lca(root, p, q)
    return lca_node

def lca(node, p, q):
    global lca_node
    if not node:
        return 0
    node_is_p_or_q = 1 if p == node or q == node else 0
    p_or_q_is_left = lca(node.left, p, q)
    p_or_q_is_right = lca(node.right, p, q)
    if node_is_p_or_q + p_or_q_is_left + p_or_q_is_right == 2:
        if not lca_node:
            lca_node = node
        return 1
    
    if node_is_p_or_q or p_or_q_is_left or p_or_q_is_right: 
        return 1
    else:
        return 0


def build_binary_tree(preorder, inorder):
    global preorder_index
    global inorder_map
    inorder_map = {}
    for i, node in enumerate(inorder):
        inorder_map[node] = i
    preorder_index = 0
    return _build_binary_tree(preorder, inorder, 0, len(inorder) - 1)
    
def _build_binary_tree(preorder, inorder, left, right):
    global preorder_index
    if left > right:
        return None
    node = TreeNode(preorder[preorder_index])
    preorder_index += 1
    inorder_index = inorder_map[node.val]
    node.left = _build_binary_tree(preorder, inorder, left, inorder_index - 1)
    node.right = _build_binary_tree(preorder, inorder, inorder_index + 1, right)
    return node
    
    
 
def max_path_sum(root):
    global max_depth
    max_depth = root.val
    dfs_max_path_sum(root)
    return max_depth

def dfs_max_path_sum(node):
    global max_depth
    if not node:
        return 0
    left = max(dfs_max_path_sum(node.left), 0)
    right = max(dfs_max_path_sum(node.right), 0)
    max_depth = max(max_depth, left + node.val + right)
    return node.val + max(left, right)
    
    
def binary_tree_symmetry(root):
    if not root:
        return True
    return dfs_binary_tree_symmetry(root.left, root.right)
    
def dfs_binary_tree_symmetry(left, right):
    if not left and right:
        return False
    elif left and not right:
        return False
    elif left and right:
        if left.val != right.val:
            return False
        return dfs_binary_tree_symmetry(left.left, right.right) and dfs_binary_tree_symmetry(left.right, right.left)
    else:
        return True
     
    
def binary_tree_columns(root):
    if not root:
        return []
    queue = deque([[0, root]])
    columns_map = defaultdict(list)
    left, right = 0, 0
    while queue:
        level_size = len(queue)
        left = min(queue[0][0], left)
        for _ in range(level_size):
            i, node = queue.popleft()
            columns_map[i].append(node.val)
            if node.left:
                queue.append([i - 1, node.left])
            if node.right:
                queue.append([i + 1, node.right])
            right = max(right, i)
    return [columns_map[i] for i in range(left, right + 1)]


def kth_smallest_number_in_BST(root, k):
    # res = []
    # inorder_recurse(root, res)
    # return res[k - 1]
    return inorder2(root, k)

def inorder_recurse(node, res = []):
    if not node:
        return
    inorder_recurse(node.left, res)
    res.append(node.val)
    inorder_recurse(node.right, res)
    
def inorder2(root, k):
    stack = []
    node = root
    
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k = k - 1
        if k == 0:
            return node.val
        node = node.right    
    
    
    

for_none = 'None'

def serialize(root):
    res = []
    dfs_preorder_serialize(root, res)
    return ",".join([str(ele) for ele in res])

def dfs_preorder_serialize(node, res = []):
    if not node:
        res.append(for_none)
        return
    res.append(node.val)
    dfs_preorder_serialize(node.left, res)
    dfs_preorder_serialize(node.right, res)
    

def deserialize(data):
    global index
    index = 0
    res = data.split(",")
    return dfs_deserialize(res)
    
def dfs_deserialize(res):
    global index
    if res[index] != for_none:
        node = TreeNode(int(res[index]))
        index += 1
        node.left = dfs_deserialize(res)
        node.right = dfs_deserialize(res)
        return node
    else:
        index += 1
        return None
        
    