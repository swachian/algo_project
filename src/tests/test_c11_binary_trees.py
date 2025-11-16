import pytest
from algo_project.c11_binary_trees import invert_binary_tree, TreeNode



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

