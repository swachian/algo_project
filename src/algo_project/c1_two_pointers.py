def pair_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return [left, right]
    return []    
        
    
def triplet_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        pairs = find_pairs_sum(nums, i + 1, 0 - nums[i])
        for pair in pairs:
            res.append([nums[i]] + pair)
    return res
        
def find_pairs_sum(nums, start, target):
    res = []
    left = start
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            res.append([nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
    return res
        
def is_palindrome_valid(s):
    slist = [c for c in s if c.isalpha() or c.isnumeric() ]
    
    left = 0
    right = len(slist) - 1
    while left < right:
        if slist[left] != slist[right]:
            return False
        left += 1
        right -= 1
    return True

def largest_container(heights):
    left = 0
    right = len(heights) - 1
    largest = 0
    while left < right:
        height = min(heights[left], heights[right])
        largest = max(largest, (right - left) * height)
        if heights[left] > heights[right]:
            right -= 1
        elif heights[right] > heights[left]:
            left += 1
        else:
            left += 1
            right -= 1
    return largest