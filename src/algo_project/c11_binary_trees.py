class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def invert_binary_tree(root):
    if not root:
        return
    
    root.left, root.right = root.right, root.left
    
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root




