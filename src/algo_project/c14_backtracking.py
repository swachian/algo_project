def find_all_permutations(nums):
    if not nums:
        return [[]]
    res = []
    bt_find_all_permutations(nums, res)
    return res

def bt_find_all_permutations(nums, res = [], candidates = [], visited = set()):
    if len(candidates) == len(nums):
        res.append(candidates[0:])
        return
    
    for num in nums:
        if num not in visited:
            candidates.append(num)
            visited.add(num)
            bt_find_all_permutations(nums, res, candidates, visited)

            candidates.pop()
            visited.remove(num)
            # bt_find_all_permutations(nums, res, candidates, visited)














































        
def find_all_subsets(nums):
    if not nums:
        return [[]]
    res = []
    bt_find_all_subsets(nums, 0, res)
    return res

def bt_find_all_subsets(nums, i, res = [], candidates = []):
    if i == len(nums):
        res.append(candidates[0:])
        return
    
    candidates.append(nums[i])
    bt_find_all_subsets(nums, i + 1, res, candidates)

    candidates.pop()
    bt_find_all_subsets(nums, i + 1, res, candidates)




    
def n_queens(n):
    global res 
    res = 0
    backtracking_n_queens(n, 0)
    return res

def backtracking_n_queens(n, i, cols = set(), angol = set(), dangol = set()):
    global res 
    if i == n:
        res += 1
        return 

    for j in range(n):
        if j in cols:
            continue
        if i + j in angol:
            continue
        if i - j in dangol:
            continue
        cols.add(j)
        angol.add(i + j)
        dangol.add(i - j)

        backtracking_n_queens(n, i + 1, cols, angol, dangol)
        
        cols.remove(j)
        angol.remove(i + j)
        dangol.remove(i - j)
            

        
def combinations_of_sum_k(nums, target):
    res = []
    bt_combinations_of_sum_k(nums, 0, target, res)
    return res

def bt_combinations_of_sum_k(nums, i, target, res = [], candidates = []):
    if target == 0:
        res.append(candidates[0:])
        return
    
    if target < 0:
        return 
    
    for j in range(i, len(nums)):
        candidates.append(nums[j])
        bt_combinations_of_sum_k(nums, j, target - nums[j], res, candidates )
        candidates.pop()




def phone_keypad_combinations(digits):
    digital_alpha_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = [] 
    backtracking_phone(digits, 0, digital_alpha_map, [], res)
    return res


def backtracking_phone(digits, i, digital_alpha_map, candidates = [], res = []):
    if i == len(digits):
        res.append(''.join(candidates))
        return
    
    for c in digital_alpha_map[digits[i]]:
        candidates.append(c)
        backtracking_phone(digits, i + 1, digital_alpha_map, candidates, res)
        candidates.pop()
