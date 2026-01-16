import pytest
from algo_project.c2_maps_and_sets import pair_sum_unsorted, verify_sudoku_board, zero_striping, longest_chain_of_consecutive_numbers, geometric_sequence_triplets

def test_pair_sum_unsorted():
    nums = [-1, 3, 4, 2]
    target = 3
    result = pair_sum_unsorted(nums, target)
    
    sorted_result = sorted([sorted(sublist) for sublist in result])
    sorted_expected = sorted([sorted(sublist) for sublist in [[0, 2]]])
    assert sorted_result == sorted_expected


def test_verify_sudoku_board():
    board = [[3,0,6,0,5,8,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1],[1,0,2,5,0,0,3,2,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[0,1,0,0,0,0,0,7,4],[0,3,0,0,0,8,2,5,0],[0,0,5,2,0,6,0,0,0]]
    result = verify_sudoku_board(board)
    assert result == False
    
    board = [[3,0,6,0,5,0,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1],[1,0,0,5,0,0,3,2,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[0,1,0,0,0,0,0,7,4],[0,3,0,0,0,8,2,5,0],[0,0,5,2,0,6,0,0,0]]
    result = verify_sudoku_board(board)
    assert result == True
    
    
def test_zero_striping():
    matrix = [[1,2,3,4,5],[6,0,6,9,10],[11,12,13,14,15],[16,17,18,19,0]]
    result = zero_striping(matrix)
    assert result == [[1,0,3,4,0],[0,0,0,0,0],[11,0,13,14,0],[0,0,0,0,0]]
    
def test_longest_chain_of_consecutive_numbers():
    nums = [1, 6, 2, 5, 8, 7, 10, 3]
    result = longest_chain_of_consecutive_numbers(nums)
    assert result == 4
    
def test_geometric_sequence_triplets():
    nums = [2, 1, 2, 4, 8, 8]
    result = geometric_sequence_triplets(nums, 2)
    assert result == 5
    
def test_geometric_sequence_triplets2():
    nums = [1,1,1,1,1]
    result = geometric_sequence_triplets(nums, 1)
    assert result == 10 
