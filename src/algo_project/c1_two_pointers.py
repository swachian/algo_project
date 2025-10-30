def pair_sum_sorted(nums, target):
    i = 0
    j = len(nums) - 1
    while j > i:
        sum = nums[i] + nums[j]
        if sum > target:
            j -=1 
        elif sum < target:
            i += 1
        else:
            return [i, j]
        
    return []

def triplet_sum(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    i = 0
    result = []
    a = None
    while i < n - 2:
        if a == sorted_nums[i]:
            i += 1
            continue
        a = sorted_nums[i]
        if a > 0:
            break
        
        j = i + 1
        k = n - 1
        while k > j:
            b = sorted_nums[j]
            sum = sorted_nums[j] + sorted_nums[k]
            if sum == -a:
                result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                j += 1
                while b == sorted_nums[j] and j < k:
                    j += 1
            elif sum < -a:
                j += 1
            else:
                k -= 1
                
    return result
    
    
def is_palindrome_valid(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True
