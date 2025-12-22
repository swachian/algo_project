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
    

def longest_chain_of_consecutive_numbers(nums):
    nums_set = set(nums)
    max_value = 0
    
    for num in nums:
        if (num - 1) not in nums_set:
            i = 1
            while (num + i) in nums_set:
                i += 1
            max_value = max(max_value, i)
        
            
    return max_value

from collections import defaultdict

def geometric_sequence_triplets(nums, r):
    left = defaultdict(int)
    right = defaultdict(int)
    result = 0
    
    for num in nums:
        right[num] += 1
    
    for num in nums:
        right[num] -= 1
        if num % r == 0:
            lnum, rnum = num / r, num * r
            result += left[lnum] * right[rnum]
        left[num] += 1
    return result