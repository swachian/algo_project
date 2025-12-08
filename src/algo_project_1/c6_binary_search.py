import random

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

def find_the_target_in_a_rotated_sorted_array(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[right]:
            if target > nums[mid] and target <= nums[right]:
                left += 1
            else:
                right -=1 
        else:
            if target >= nums[left] and target < nums[mid]:
                right -= 1
            else:
                left += 1
                  
    return left if nums and nums[left] == target else -1

def find_the_median_from_two_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2, = nums2, nums1
        
    m, n = len(nums1), len(nums2)
    left = 0
    right = m - 1
    half_size = m + (n - m) // 2
    
    while True:
        l1_index = left + (right - left) // 2
        l2_index = half_size - (l1_index + 1) - 1
        
        L1 = float("-inf") if l1_index < 0 else nums1[l1_index]
        R1 = float("inf") if l1_index >= m - 1 else nums1[l1_index + 1]
        L2 = float("-inf") if l2_index < 0 else nums2[l2_index]
        R2 = float("inf") if l2_index >= n - 1 else nums2[l2_index + 1]
        
        if L1 > R2:
            right = l1_index - 1
        elif L2 > R1:
            left = l1_index + 1
        else:
            if (m + n) % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2
            else:
                return min(R1, R2)
        
def matrix_search(matrix, target):
    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0
    
    left = 0
    right = m * n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        r = mid // n
        c = mid % n
        value = matrix[r][c]
        if value > target:
            right = mid - 1
        elif value < target:
            left = mid + 1
        else:
            return True
        
    return False

def local_maxima_in_array(nums):
    n = len(nums)
    left = 0
    right = n - 1
    
    while left < right:
        mid = left + (right - left) // 2
        value = nums[mid]
        right_value = int("-inf") if mid >= n - 1 else nums[mid + 1]
        if right_value > value:
            left = mid + 1 
        else:
            right = mid
            
    return nums[left]

class WeightedRandomSelection:
    def __init__(self, weights):
        self.weights = [weights[0]]
        for i in range(1, len(weights)):
            self.weights.append(weights[i] + self.weights[-1])
            
    
    def select(self):
        left = 0
        right = len(self.weights) - 1
        
        target = random.randint(1, self.weights[-1])
        while left < right:
            mid = left + (right - left) // 2
            if self.weights[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
                