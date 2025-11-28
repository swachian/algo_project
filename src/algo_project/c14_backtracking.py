def find_all_permutations(nums):
    # 回溯搭配递归或栈的遍历。这道题就是把可能的组合放到candidates中，合格的candidate是len与permutation一致的
    # 需要注意的是数组加入结果集合时，因为candidate会被修改，所以需要重新复制一个
    res = []
    dfs_find_all_permutations(nums, [], set(), res)
    return res

def dfs_find_all_permutations(nums, candidates = [], visitored = set(), res = []):
    if len(candidates) == len(nums):
        res.append(candidates[:])
        return
    
    for num in nums:
        if num in visitored:
            continue
        candidates.append(num)
        visitored.add(num)
        dfs_find_all_permutations(nums, candidates, visitored, res)
        visitored.remove(num)
        candidates.pop()
        
def find_all_subsets(nums):
    # 与前一题很类似，只是这次从排列决定切换成立二叉树决定，并使用了i作为index来遍历数组。
    res = []
    backtrack_find_all_subsets(nums, [], 0, res)
    return res

def backtrack_find_all_subsets(nums, candidates, i, res):
    if i == len(nums):
        res.append(candidates[:])
        return
    
    candidates.append(nums[i])
    backtrack_find_all_subsets(nums, candidates, i + 1, res)
    candidates.pop()
    backtrack_find_all_subsets(nums, candidates, i + 1, res)
    
def n_queens(n):
    # 利用cols和两个diag的hash,比较巧妙的是diag利用r-c和r+c实现了编号
    # 遇到不能填的col,需要继续执行下一个c,而不是return
    global res
    res = 0
    backtrack_n_queens(0, set(), set(), set(), n)
    return res
    

def backtrack_n_queens(row, cols, dial1, dial2, n):
    global res
    if row == n:
        res += 1
        return
    
    for c in range(n):
        if c in cols or (row - c) in dial1 or (row + c) in dial2:
            continue
        cols.add(c)
        dial1.add(row - c)
        dial2.add(row + c)
        backtrack_n_queens(row + 1, cols, dial1, dial2, n)
        
        cols.remove(c)
        dial1.remove(row - c)
        dial2.remove(row + c)
        
    