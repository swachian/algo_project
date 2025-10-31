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