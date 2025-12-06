import pytest
from algo_project.c19_maths import spiral_matrix



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


