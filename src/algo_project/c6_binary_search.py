def find_the_insertion_index(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right  - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
            
    return left

def first_and_last_occurrences_of_a_number(nums, target):
    target_index = find_the_insertion_index(nums, target)
    n = len(nums)
    if target_index == n or nums[target_index] != target:
        return [-1, -1]
    left = find_left_most(nums, target_index)
    right = find_right_most(nums, target_index)
    return [left, right]
    
def find_left_most(nums, target_index):
    target = nums[target_index]
    left, right = 0, target_index
    while left < right:
        mid = left + (right - left) // 2 
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def find_right_most(nums, target_index):
    target = nums[target_index]
    left, right = target_index, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid
    return left

def cutting_wood(heights, k):
    left, right = 0, max(heights)
    while left < right:
        mid = left + (right - left) // 2 + 1
        if is_at_least_k(heights, mid, k):
            left = mid
        else:
            right = mid - 1
    return right 

def is_at_least_k(heights, h, k):
    sum = 0
    for n in heights:
        sum += n - h if n - h > 0 else 0
    
    return sum >= k