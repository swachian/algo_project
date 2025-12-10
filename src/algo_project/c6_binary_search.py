def find_the_insertion_index(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid 
        else:
            return mid
    return left

def first_and_last_occurrences_of_a_number(nums, target):
    if not nums:
        return [-1, -1]
    left = low_bound_search(nums, target)
    right = high_bound_search(nums, target)
    return [left, right]
    
def low_bound_search(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            right = mid
            
    return left if nums[left] == target else -1

def high_bound_search(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else: 
            left = mid
    return left if nums[left] == target else - 1

def cutting_wood(heights, k):
    left, right = 0, max(heights)
    while left < right:
        mid = left + (right - left) // 2 + 1
        cuts = compute_cuts(heights, mid)
        if cuts == k:
            return mid
        elif cuts < k:
            right = mid - 1
        else:
            left = mid
    return left
        
        
def compute_cuts(heights, pov):
    res = 0
    for height in heights:
        res += (height - pov) if height > pov else 0
    return res 

def find_the_target_in_a_rotated_sorted_array(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid -1
    return left if nums[left] == target else -1
            