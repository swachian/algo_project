import pytest
from algo_project.c11_binary_trees import invert_binary_tree, TreeNode, balanced_binary_tree_validation, rightmost_nodes_of_a_binary_tree, widest_binary_tree_level, binary_search_tree_validation, lowest_common_ancestor, build_binary_tree



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