def pair_sum_unsorted(nums, target):
    result = []
    maps = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in maps:
            result.append([maps[complement], i])
        maps[num] = i
    return result


def verify_sudoku_board(board):
    n = len(board)
    row_sets = [set() for _ in range(n)]
    col_sets = [set() for _ in range(n)]
    grid_sets = [[set() for i in range(n // 3)] for _ in range(n // 3)]
    
    # print(row_sets)

    for i in range(n):
        for j in range(n):
            c = board[i][j]
            if c == 0:
                continue
            if c in row_sets[i]:
                return False
            if c in col_sets[j]:
                return False
            if c in grid_sets[i // 3][j // 3]:
                return False
            row_sets[i].add(c)
            col_sets[j].add(c)
            grid_sets[i // 3][j // 3].add(c)
    return True
        
    
    
    
def zero_striping(matrix):
    first_col_has_zero = False
    first_row_has_zero = False
    
    if not matrix:
        return matrix
    m, n = len(matrix), len(matrix[0]) 
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_has_zero = True
            break
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0
    return matrix

    
from collections import defaultdict
def longest_chain_of_consecutive_numbers(nums):
    nums_set = set(nums)

    max_count = 0
    for num in nums:
        c = num - 1
        if c not in nums_set:
            count = 1
            while num + 1 in nums_set:
                num += 1
                count += 1
            max_count = max(max_count, count)
    return max_count

from collections import defaultdict

def geometric_sequence_triplets(nums, r):
    left_count = defaultdict(int)
    right_count = defaultdict(int)
    for num in nums:
        right_count[num] += 1

    res = 0
    for num in nums:
        right_count[num] -= 1
        if num % r == 0:
            l = num // r
            right = num * r
            res += left_count[l] * right_count[right]
        left_count[num] += 1
    
    return res
