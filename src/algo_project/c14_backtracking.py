def find_all_permutations(nums):
    if not nums:
        return [[]]
    res = []
    backtracking_find_all_permutations(nums, set(), [], res)
    return res
    
def backtracking_find_all_permutations(nums, visited = set(), candidates = [], res = []):
    if len(candidates) == len(nums):
        res.append(candidates[0:])
        return 
    for num in nums:
        if num not in visited:
            candidates.append(num)
            visited.add(num)
            backtracking_find_all_permutations(nums, visited, candidates, res)

            candidates.pop()
            visited.remove(num)















































        
def find_all_subsets(nums):
    if not nums:
        return [[]]
    res = []
    backtracking_find_all_subsets(nums, 0, [], res)
    return res

def backtracking_find_all_subsets(nums, i, candidates = [], res = []):
    if i == len(nums):
        res.append(candidates[0:])
        return 
    candidates.append(nums[i])
    backtracking_find_all_subsets(nums, i + 1, candidates, res)

    candidates.pop()
    backtracking_find_all_subsets(nums, i + 1, candidates, res)
    



    
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
    backtracking_combinations_of_sum_k(nums, 0, [], target, res)
    return res

def backtracking_combinations_of_sum_k(nums, i, candidates, target, res):
    if target == 0:
        res.append(candidates[0:])
        return 
    if target < 0:
        return
    
    for j in range(i, len(nums)):
        candidates.append(nums[j])
        backtracking_combinations_of_sum_k(nums, j, candidates, target - nums[j], res)
        candidates.pop()
        # backtracking_combinations_of_sum_k(nums, j, candidates, target, res)



def phone_keypad_combinations(digits):
    digital_alpha_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []
    backtracking_phone_keypad_combinations(digits, 0, digital_alpha_map, [], res)
    return res
    
def backtracking_phone_keypad_combinations(digits, i, digital_alpha_map, candidates = [], res = []):
    if len(candidates) == len(digits):
        res.append(''.join(candidates[0:]))
        return 
    
    for c in digital_alpha_map[digits[i]]:
        candidates.append(c)
        backtracking_phone_keypad_combinations(digits, i + 1, digital_alpha_map, candidates, res)
        candidates.pop()
   