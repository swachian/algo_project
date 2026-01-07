def find_all_permutations(nums):
    # 回溯搭配递归或栈的遍历。这道题就是把可能的组合放到candidates中，合格的candidate是len与permutation一致的
    # 每次调用前从nums中挑选一个给到candidate,然后递归调用时再次遍历所有未访问的元素，回溯时则把刚刚加入的元素都退出来，便于循环使用后一个组合
    # 需要注意的是数组加入结果集合时，因为candidate会被修改，所以需要重新复制一个
    res = []
    dfs_find_all_permutations(nums, [], set(), res)
    return res

def dfs_find_all_permutations(nums, cadidates, visited, res):
    if len(cadidates) == len(nums):
        res.append(cadidates[:])
        return
    for num in nums:
        if num not in visited:
            cadidates.append(num)
            visited.add(num)
            dfs_find_all_permutations(nums, cadidates, visited, res)
            
            cadidates.pop()
            visited.remove(num)
        
    

def find_all_subsets(nums):
    # 与前一题很类似，只是这次从排列决定切换成立二叉树决定，并使用了i作为index来遍历数组。
    res = []
    dfs_find_all_subsets(nums, 0, [], res)
    return res

def dfs_find_all_subsets(nums, i, candidates, res):
    if i == len(nums):
        res.append(candidates[:])
        return
    
    candidates.append(nums[i])
    dfs_find_all_subsets(nums, i + 1, candidates, res)
    
    candidates.pop()
    dfs_find_all_subsets(nums, i + 1, candidates, res)


def n_queens(n):
    # 利用cols和两个diag的hash,比较巧妙的是diag利用r-c和r+c实现了编号
    # 遇到不能填的col,需要继续执行下一个c,而不是return
    global res
    res = 0
    dfs_n_queens(0, set(), set(), set(), n)
    return res
    
def dfs_n_queens(row, cols_map, angols_map, dangols_map, n):
    global res
    if row == n:
        res += 1
        return
    
    for c in range(n):
        if c in cols_map:
            continue
        if (row - c) in angols_map:
            continue
        if (row + c) in dangols_map:
            continue
        cols_map.add(c)
        angols_map.add(row - c)
        dangols_map.add(row + c)
        dfs_n_queens(row + 1, cols_map, angols_map, dangols_map, n)
        
        cols_map.remove(c)
        angols_map.remove(row - c)
        dangols_map.remove(row + c)
        
def combinations_of_sum_k(nums, target):
    res = []
    backtrack_combinations_of_sum_k(nums, 0, [], target, res)
    return res

def backtrack_combinations_of_sum_k(nums, start_index, candidates, target, res):
    # 手法和find_all_permutations很类似，但加了每次遍历的start_index来避免类似的组合
    # 而start_index递增是利用的for循环的自然递增，其他方面则和permutation高度类似
    if target == 0:
        res.append(candidates[:])
        return
    
    if target < 0:
        return
    
    for i in range(start_index, len(nums)):
        candidates.append(nums[i])
        backtrack_combinations_of_sum_k(nums, i, candidates, target - nums[i], res)
        candidates.pop()
        
        
def phone_keypad_combinations(digits):
    # 这题比较简单，然后发现回溯和数的遍历最大的区别在于2点：
    # 1. 树的遍历一般是二叉树，回溯可能有多个决策
    # 2. 回溯总有一个pop返回之前的选择，这可能就是backtrack的本意，即后悔了然后重新选
    res = []
    digital_alpha_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    backtracking_phone_keypad_combinations(0, digits, digital_alpha_map, [], res)
    return res

def backtracking_phone_keypad_combinations(i, digits, digital_alpha_map, candidates, res):
    if len(candidates) == len(digits):
        if len(candidates) > 0:
            res.append("".join(candidates)) 
        return
    
    for c in digital_alpha_map[digits[i]]:
        candidates.append(c)
        backtracking_phone_keypad_combinations(i + 1, digits, digital_alpha_map, candidates, res)
        candidates.pop()