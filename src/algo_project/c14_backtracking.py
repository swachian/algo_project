def find_all_permutations(nums):
    if not nums:
        return [[]]
    res = []
    backtrack_find_all_permutations(nums, [], set(), res)
    return res

def backtrack_find_all_permutations(nums, candidates = [], visited = set(), res = []):
    if len(candidates) == len(nums):
        res.append(candidates[0:])
        return
    
    for num in nums:
        if num not in visited:
            visited.add(num)
            candidates.append(num)
            backtrack_find_all_permutations(nums, candidates, visited, res)

            visited.remove(num)
            candidates.pop()
















































        
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
    res = []
    backtrack_combinations_of_sum_k(nums, 0, target, [], res)
    return res

def backtrack_combinations_of_sum_k(nums, start_index, target, candidates = [], res = []):
    if target < 0:
        return 
    if target == 0:
        res.append(candidates[0:])
    
    for i in range(start_index, len(nums)):
        candidates.append(nums[i])
        backtrack_combinations_of_sum_k(nums, i, target - nums[i], candidates, res)
        candidates.pop()

def phone_keypad_combinations(digits):
    digital_alpha_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []
    backtracking_phone_keypad_combinations(digital_alpha_map, digits, 0, [], res)
    return res

def backtracking_phone_keypad_combinations(da_map, digits, i, candidates = [], res = []):
    if i == len(digits):
        res.append(''.join(candidates)) 
        return 
    for c in da_map[digits[i]]:
        candidates.append(c)
        backtracking_phone_keypad_combinations(da_map, digits, i + 1, candidates, res)

        candidates.pop()