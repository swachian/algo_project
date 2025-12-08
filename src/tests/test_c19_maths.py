import pytest
from algo_project.c19_maths import spiral_matrix, reverse_32_bit_integer, gcd, maximum_collinear_points, compute_slope



import pytest

def test_spiral_matrix_square():
    # A simple 3x3 matrix
    # Spiral order: 1 → 2 → 3 → 6 → 9 → 8 → 7 → 4 → 5
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = spiral_matrix(matrix)
    assert result == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_spiral_matrix_rectangle():
    # A 3x4 rectangle matrix
    # Spiral order: 1 → 2 → 3 → 4 → 8 → 12 → 11 → 10 → 9 → 5 → 6 → 7
    matrix = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12]
    ]
    assert spiral_matrix(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test_reverse_positive_integer():
    # Normal positive number within 32-bit range
    # 123 → 321
    assert reverse_32_bit_integer(123) == 321


def test_reverse_overflow():
    # This reversed result overflows 32-bit signed integer range
    # 1534236469 → reversed = 9646324351 (overflow) → return 0
    assert reverse_32_bit_integer(1534236469) == 0

def test_gcd1():
    a = gcd(13, 26)
    assert a == 13
    assert gcd(3, 0) == 3
    
def test_gcd2():
    a = gcd(5, 6)
    assert a == 1
    


def test_basic_collinear():
    points = [[1,1],[1,2],[1,3],[1,4]]
    assert maximum_collinear_points(points) == 4
    
    # 3 个点在同一直线上：(1,1)、(2,2)、(3,3)
    points = [[1, 1], [2, 2], [3, 3], [1, 2]]
    assert maximum_collinear_points(points) == 3
    


def test_multiple_lines():
    # 两条“直线群”：
    # Line A: (0,0), (1,1), (2,2), (3,3) ⇒ 4 个点
    # Line B: (0,1), (0,2), (0,3) ⇒ 3 个点
    points = [
        [0, 0], [1, 1], [2, 2], [3, 3],
        [0, 1], [0, 2], [0, 3],
        [5, 4],
    ]
    assert maximum_collinear_points(points) == 4

def test_compute_slope():
    assert compute_slope((0, 0), (1, 2)) == (2, 1)
    assert compute_slope((1, 2), (14, 28)) == (2, 1)