import pytest
from algo_project.c11_binary_trees import invert_binary_tree, TreeNode, balanced_binary_tree_validation, rightmost_nodes_of_a_binary_tree, widest_binary_tree_level, binary_search_tree_validation, lowest_common_ancestor, build_binary_tree, max_path_sum
from algo_project.c11_binary_trees import binary_tree_symmetry, binary_tree_columns


def test_invert_tree_basic():
    # Build tree:
    #     4
    #    / \
    #   2   7
    #  / \ / \
    # 1  3 6  9
    root = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9))
    )

    inverted = invert_binary_tree(root)

    # Expected tree:
    #     4
    #    / \
    #   7   2
    #  / \ / \
    # 9  6 3  1
    assert inverted.left.val == 7
    assert inverted.right.val == 2
    assert inverted.left.left.val == 9
    assert inverted.left.right.val == 6
    assert inverted.right.left.val == 3
    assert inverted.right.right.val == 1

def test_invert_tree_single_node():
    root = TreeNode(1)

    inverted = invert_binary_tree(root)

    # A single node tree should remain the same
    assert inverted.val == 1
    assert inverted.left is None
    assert inverted.right is None

def test_balanced_tree():
    # Balanced tree:
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root = TreeNode(3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )

    assert balanced_binary_tree_validation(root) is True
    
def test_unbalanced_tree():
    # Unbalanced tree:
    #        1
    #       /
    #      2
    #     /
    #    3
    #   /
    #  4
    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(
                3,
                TreeNode(4)
            )
        )
    )

    assert balanced_binary_tree_validation(root) is False
    
def test_rightmost_nodes_basic():
    # Tree:
    #       1
    #     /   \
    #    2     3
    #     \
    #      5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    assert rightmost_nodes_of_a_binary_tree(root) == [1, 3, 5]


def test_rightmost_nodes_left_heavy():
    # Tree:
    #       10
    #      /
    #     6
    #    /
    #   4
    root = TreeNode(10, TreeNode(6, TreeNode(4), None), None)

    assert rightmost_nodes_of_a_binary_tree(root) == [10, 6, 4]


def test_widest_level_sparse_tree():
    # Tree:
    #           1
    #         /   \
    #        2     3
    #       /       \
    #      4         5
    #
    # Level widths:
    # level 0: [1] → 1
    # level 1: [2,3] → 2
    # level 2: [4,null,null,5] → index difference = 3 - 0 + 1 = 4
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4))
    root.right = TreeNode(3, None, TreeNode(5))

    assert widest_binary_tree_level(root) == 4


def test_widest_level_full_tree():
    # Tree:
    #          10
    #        /    \
    #       6      8
    #      / \    / \
    #     1   2  3   4
    #
    # Each level widths:
    # level 0 = 1
    # level 1 = 2
    # level 2 = 4 (full)
    root = TreeNode(10)
    root.left = TreeNode(6, TreeNode(1), TreeNode(2))
    root.right = TreeNode(8, TreeNode(3), TreeNode(4))

    assert widest_binary_tree_level(root) == 4
    
def test_valid_bst():
    # Valid BST:
    #        5
    #      /   \
    #     3     7
    #    / \   / \
    #   2  4  6   8
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(7, TreeNode(6), TreeNode(8))

    assert binary_search_tree_validation(root) is True


def test_invalid_bst():
    # Invalid because 6 is in the left subtree of 5
    #        5
    #      /
    #     3
    #      \
    #       6   ← violates BST rule
    root = TreeNode(5)
    root.left = TreeNode(3, None, TreeNode(6))

    assert binary_search_tree_validation(root) is False
    
def test_lca_common_case():
    # Tree:
    #        3
    #      /   \
    #     5     1
    #    / \   / \
    #   6  2  0   8
    #
    # LCA(5, 1) = 3

    root = TreeNode(3)
    root.left = TreeNode(5, TreeNode(6), TreeNode(2))
    root.right = TreeNode(1, TreeNode(0), TreeNode(8))

    p = root.left
    q = root.right

    assert lowest_common_ancestor(root, p, q).val == 3


def test_lca_node_is_ancestor():
    # Tree:
    #      5
    #     /
    #    3
    #   /
    #  2
    #
    # LCA(5, 2) = 5  (ancestor of itself)
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2))

    p = root
    q = root.left.left

    assert lowest_common_ancestor(root, p, q).val == 5
    
def serialize(root):
    """Serialize tree into list (preorder) for testing purposes."""
    if not root:
        return None
    return [root.val, serialize(root.left), serialize(root.right)]

def test_build_tree_basic():
    preorder = [5, 9, 2, 3, 4, 7]
    inorder = [2, 9, 5, 4, 3, 7]

    root = build_binary_tree(preorder, inorder)

    # Expected tree structure serialized
    assert serialize(root) == [
        5,
        [9, [2, None, None], None],
        [3, [4, None, None], [7, None, None]]
    ]


def test_build_tree_single_node():
    preorder = [10]
    inorder = [10]

    root = build_binary_tree(preorder, inorder)

    assert serialize(root) == [10, None, None]
    
# Test 1: A balanced binary tree
def test_maxPathSum_balanced():
    # Constructing a balanced tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    assert max_path_sum(root) == 17  # Maximum path sum: 4 + 2 + 1 + 3 + 6 = 16

# Test 2: A tree with negative values
def test_maxPathSum_negative():
    # Constructing a tree with negative values:
    #        -10
    #       /    \
    #     9      20
    #           /  \
    #         15   7
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    assert max_path_sum(root) == 42  # Maximum path sum: 15 + 20 + 7 = 42
    
# Test 1: A symmetric binary tree
def test_isSymmetric_symmetric():
    # Constructing a symmetric tree:
    #        1
    #       / \
    #      2   2
    #     / \ / \
    #    3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    
    assert binary_tree_symmetry(root) == True  # The tree is symmetric

# Test 2: A non-symmetric binary tree
def test_isSymmetric_non_symmetric():
    # Constructing a non-symmetric tree:
    #        1
    #       / \
    #      2   2
    #     / \   \
    #    3   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    
    assert binary_tree_symmetry(root) == False  # The tree is not symmetric
    
# Test 1: A basic binary tree
def test_verticalOrder_basic():
    # Constructing a simple tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    expected_output = [
        [4],  # Column -1
        [2],  # Column 0
        [1, 5],  # Column 1
        [3]   # Column 2
    ]

    assert binary_tree_columns(root) == expected_output

# Test 2: A more complex binary tree
def test_verticalOrder_complex():
    # Constructing a more complex tree:
    #           1
    #         /   \
    #        2     3
    #       / \   / \
    #      4   5 6   7
    #     /        /  \
    #    8        9    10
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.right.right = TreeNode(10)

    expected_output = [
        [8],     # Column -2
        [4],     # Column -1
        [2],     # Column 0
        [1, 5, 6],  # Column 1
        [3, 9],     # Column 2
        [7],     # Column 3
        [10]  # Column 4
    ]

    assert binary_tree_columns(root) == expected_output