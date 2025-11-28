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