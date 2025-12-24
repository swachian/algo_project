def pair_sum_unsorted(nums, target):
    results = []
    pairs = {}
    for index, num in enumerate(nums):
        sub = target - num
        if sub in pairs:
            results.append([index, pairs[sub]])
        pairs[num] = index
    
    return results

def verify_sudoku_board(board):
    n = len(board)
    row_numbers = [set() for _ in range(n)] 
    col_numbers = [set() for _ in range(n)] 
    rect_numbers = [[set() for _ in range(3)]  for i in range(n // 3)]
    
    for i in range(n):
        for j in range(n):
            c = board[i][j]
            if c == 0:
                continue
            if c in row_numbers[i]:
                return False
            if c in col_numbers[j]:
                return False
            if c in rect_numbers[i // 3][j // 3]:
                return False
            row_numbers[i].add(c)
            col_numbers[j].add(c)
            rect_numbers[i // 3][j // 3].add(c)
    return True

def zero_striping(matrix):
    first_row_has_zero = False
    first_col_has_zero = False
    
    if not matrix or not matrix[0]:
        return 
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_has_zero = True
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_has_zero = True
            
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0
                
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
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
    nums_map = {}
    for num in nums:
        nums_map[num] = 1

    max_count = 0
    for i in range(len(nums)):
        num = nums[i]
        if (num - 1) not in nums_map:
            count = 1
            while num + 1 in nums_map:
                count += 1
                num = num + 1
            max_count = max(max_count, count)
    return max_count

from collections import defaultdict

def geometric_sequence_triplets(nums, r):
    left_set = defaultdict(int)
    right_set = defaultdict(int)

    # nums.sort()
    for num in nums:
        right_set[num] += 1
    max_count = 0
    for num in nums:
        right_set[num] -= 1
        if num % r == 0:
            left_num = num // r
            right_num = num * r
            if left_num in left_set and right_num in right_set:
                max_count += left_set[left_num] * right_set[right_num]
        left_set[num] += 1
        
    return max_count