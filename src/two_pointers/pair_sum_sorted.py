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