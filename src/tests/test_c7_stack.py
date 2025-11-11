import pytest
from algo_project.c7_stack import valid_parenthesis_expression, next_largest_number_to_the_right, evaluate_expression, repeated_removal_of_adjacent_duplicates, maximums_of_sliding_window


def test_valid_parentheses_balanced():
    """Test a valid and properly nested parenthesis string."""
    expr = "{[()()]}"
    assert valid_parenthesis_expression(expr) is True


def test_valid_parentheses_unbalanced():
    """Test an invalid parenthesis string where closing order is incorrect."""
    expr = "((())"
    assert valid_parenthesis_expression(expr) is False
    
def test_next_largest_number_basic():
    """Test with a mixed array where some elements have larger numbers to the right."""
    nums = [2, 1, 2, 4, 3]
    expected = [4, 2, 4, -1, -1]
    assert next_largest_number_to_the_right(nums) == expected


def test_next_largest_number_no_larger():
    """Test when no element has a larger number to its right."""
    nums = [5, 4, 3, 2, 1]
    expected = [-1, -1, -1, -1, -1]
    assert next_largest_number_to_the_right(nums) == expected    
    
def test_evaluate_expression_simple():
    """Test simple expression with addition and subtraction."""
    expr = "1 + 2 - 3 + 4"
    assert evaluate_expression(expr) == 4


def test_evaluate_expression_with_parentheses():
    """Test expression with nested parentheses and mixed operators."""
    expr = "(1 + (2 - 3)) + (4 - (1 - 2))"
    # (1 + (2 - 3)) + (4 - (1 - 2)) = (0) + (4 - (-1)) = 5
    assert evaluate_expression(expr) == 5
    
def test_remove_adjacent_duplicates_basic():
    """Test simple case where adjacent duplicates appear once."""
    s = "abbaca"
    # Remove "bb" → "aaca" → remove "aa" → "ca"
    assert repeated_removal_of_adjacent_duplicates(s) == "ca"


def test_remove_adjacent_duplicates_multiple_passes():
    """Test when multiple rounds of removals are needed."""
    s = "azxxzy"
    # Remove "xx" → "azzy" → remove "zz" → "ay"
    assert repeated_removal_of_adjacent_duplicates(s) == "ay"
    
    
def test_basic_case_maximums_of_sliding_window():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # windows:
    # [1,3,-1] → 3
    # [3,-1,-3] → 3
    # [-1,-3,5] → 5
    # [-3,5,3] → 5
    # [5,3,6] → 6
    # [3,6,7] → 7
    assert maximums_of_sliding_window(nums, k) == [3, 3, 5, 5, 6, 7]

def test_edge_and_increasing_sequence_maximums_of_sliding_window():
    nums = [1, 2, 3, 4, 5]
    k = 2
    # windows: [1,2], [2,3], [3,4], [4,5]
    assert maximums_of_sliding_window(nums, k) == [2, 3, 4, 5]

def test_single_window_maximums_of_sliding_window():
    nums = [10, 5, 2]
    k = 3
    assert maximums_of_sliding_window(nums, k) == [10]