def find_all_permutations(nums):
    res = []
    dfs_find_all_permutations(nums, [], set(), res)
    return res

def dfs_find_all_permutations(nums, candidates = [], visited = set(), res = []):
    if len(candidates) == len(nums):
        res.append(candidates[0:])
        return 
    for num in nums:
        if num in visited:
            continue
        candidates.append(num)
        visited.add(num)
        dfs_find_all_permutations(nums, candidates, visited, res)

        candidates.pop()
        visited.remove(num)
        # dfs_find_all_permutations(nums, candidates, visited, res)
        
def find_all_subsets(nums):
    res = []
    dfs_find_all_subsets(nums, 0, [], res)
    return res

def dfs_find_all_subsets(nums, i, candidates = [], res = []):
    if i == len(nums):
        res.append(candidates[0:])
        return
    
    candidates.append(nums[i])
    dfs_find_all_subsets(nums, i + 1, candidates, res)

    candidates.pop()
    dfs_find_all_subsets(nums, i + 1, candidates, res)
    
def n_queens(n):
    global res 
    res = 0
    backtracking_n_queens(0, n)
    return res

def backtracking_n_queens(r, n, cols = set(), angels = set(), dangels = set()):
    global res
    if r == n:
        res += 1
        return 
        
    for c in range(n):
        if c in cols:
            continue
        if r + c in angels:
            continue
        if r - c in dangels:
            continue
        cols.add(c)
        angels.add(r + c)
        dangels.add(r - c)

        backtracking_n_queens(r + 1, n, cols, angels, dangels)
        
        cols.remove(c)
        angels.remove(r + c)
        dangels.remove(r -c )
        
def combinations_of_sum_k(nums, target):
    if not nums:
        return []
    res = []
    backtracking_combinations_of_sum_k(nums, 0, target, [], res)
    return res

def backtracking_combinations_of_sum_k(nums, i, target, candidates = [], res = []):
    if target == 0:
        res.append(candidates[0:])
        return 
    if target < 0:
        return 
    
    for j in range(i, len(nums)):
        candidates.append(nums[j])
        backtracking_combinations_of_sum_k(nums, j, target - nums[j], candidates, res)
        
        candidates.pop()
        # backtracking_combinations_of_sum_k(nums, j, target, candidates, res)
