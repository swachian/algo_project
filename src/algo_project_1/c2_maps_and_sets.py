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
    m = len(board)
    rowset = [set() for _ in range(m)]
    colset = [set() for _ in range(m)]
    gridset = [[set(), set(), set()] for _ in range(m//3)]
    
    for i in range(m):
        for j in range(m):
            ele = board[i][j]
            if ele == 0:
                continue
            if ele in rowset[i]:
                return False
            rowset[i].add(ele)
            
            if ele in colset[j]:
                return False
            colset[j].add(ele)
            
            if ele in gridset[i//3][j//3]:
                # print(f"{i} {j}")
                return False
            gridset[i//3][j//3].add(ele)

    return True

def zero_striping(matrix):
    first_row_zero = False
    first_col_zero = False
    
    m = len(matrix)
    n = len(matrix[0])
    
    i = 0
    for j in range(n):
        if matrix[i][j] == 0:
            first_row_zero = True
            break
    j = 0 
    for i in range(m):
        if matrix[i][j] == 0:
            first_col_zero = True
            break
    
    for i in range(1, m):
        for j in range(1, n):
            # if matrix[0][j] == 0 and matrix[i][0] == 0:
            #     continue
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
    return matrix

def longest_chain_of_consecutive_numbers(nums):
    nums_set = set(nums)
    max_consecutive = 0
    for num in nums:
        if (num - 1) not in nums_set:
            count = 1
            next_num = num + 1
            while next_num in nums_set:
                next_num += 1
                count += 1
            max_consecutive = max(max_consecutive, count)
            
    return max_consecutive

def geometric_sequence_triplets(nums, r):
    result = 0
    num_maps_left = {}
    num_maps_right = {}
    
    for num in nums:
        num_maps_right[num] = num_maps_right.get(num, 0) + 1
    
    for num in nums:
        num_maps_right[num] -= 1
        if num % r == 0:
            a = num // r
            c = num * r
            if a in num_maps_left and c in num_maps_right:
                result += num_maps_right[c] * num_maps_left[a]
        num_maps_left[num] = num_maps_left.get(num, 0) + 1
                
        
    return result