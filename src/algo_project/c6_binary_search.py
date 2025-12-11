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
            
def find_the_median_from_two_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    half_len = (m + n) // 2
    left = 0
    right = m - 1
    while True:
        L1_index = left + (right - left)  // 2
        L2_index = half_len - (L1_index + 1) - 1
        L1 = nums1[L1_index] if L1_index >= 0 else float("-inf")
        R1 = nums1[L1_index + 1] if L1_index < m - 1 else float("inf")
        L2 = nums2[L2_index] if L2_index >= 0 else float("-inf")
        R2 = nums2[L2_index + 1] if L2_index < n - 1 else float("inf")
        
        if L1 > R2:
            right = L1_index - 1
        elif L2 > R1:
            left = L1_index + 1
        else:     
            if (m + n) % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2
            else:
                return min(R1, R2)
            
def matrix_search(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m = len(matrix)
    n = len(matrix[0])
    
    top, bottom = 0, m - 1
    mid_find = -1
    while top <= bottom:
        mid_i = top + (bottom - top) // 2
        if matrix[mid_i][0] <= target <= matrix[mid_i][n - 1]:
            mid_find = mid_i
            break
        elif matrix[mid_i][n - 1] < target:
            top = mid_i + 1
        else:
            bottom = mid_i - 1
    if mid_find != -1:
        left, right = 0, n - 1
        while left < right:
            mid_j = left + (right - left) // 2
            if matrix[mid_find][mid_j] == target:
                return True
            elif matrix[mid_find][mid_j] > target:
                right = mid_j - 1
            else:
                left = mid_j + 1
        return matrix[mid_find][left] == target
    
    return False
            
            
            
def local_maxima_in_array(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if (nums[mid] < nums[mid + 1]):
            left = mid + 1
        else:
            right = mid
    return right

import random
class WeightedRandomSelection:
    def __init__(self, weights):
        self.weights = [weights[0]]
        for i in range(1, len(weights)):
            self.weights.append(weights[i] + self.weights[-1])
    
    def select(self):
        left, right = 0, len(self.weights) - 1
        target = random.randint(1, self.weights[-1])
        while left < right:
            mid = left + (right - left) // 2
            if self.weights[mid] < target:
                left = mid + 1
            elif self.weights[mid] >= target:
                right = mid

        return left
            
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