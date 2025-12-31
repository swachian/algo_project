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
    lower = first_and_last_occurrences_of_a_number_lower_bound(nums, target, 0, len(nums) - 1)
    upper = first_and_last_occurrences_of_a_number_upper_bound(nums, target, 0, len(nums) - 1)
    return [lower, upper]
    

def first_and_last_occurrences_of_a_number_lower_bound(nums, target, left, right):
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left if nums[left] == target else -1
    
def first_and_last_occurrences_of_a_number_upper_bound(nums, target, left, right):
    while left < right:
        mid = left + (right - left) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid

    return left if nums[left] == target else -1
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def cutting_wood(heights, k):
    left, right = 0, max(heights)
    while left < right:
        cut_point = left + (right - left) // 2 + 1
        wood_cut = compute_wood(heights, cut_point)
        if wood_cut < k:
            right = cut_point - 1
        elif wood_cut == k:
            return cut_point
        else:
            left = cut_point
    return left
    
def compute_wood(heights, cut_point):
    sum = 0
    for height in heights:
        if height > cut_point:
            sum += height - cut_point 
    return sum    

        


def find_the_target_in_a_rotated_sorted_array(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return left if nums[left] == target else -1
            
            
            
            
            
            
            
            
def find_the_median_from_two_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)

    half_size = m + (n - m) // 2
    
    left, right = 0, m - 1
    while True:
        mid = left + (right - left) // 2
        mid2 = half_size - 2 - mid
        L1 = nums1[mid] if mid >= 0 else float("-inf")
        R1 = nums1[mid + 1] if mid <= m - 2 else float("inf")
        L2 = nums2[mid2] if mid2 >= 0 else float("-inf")
        R2 = nums2[mid2 + 1] if mid2 <= n - 2 else float("inf") 
        if R1 < L2:
            left = mid + 1
        elif L1 > R2:
            right = mid - 1
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
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left




































import random
class WeightedRandomSelection:
    def __init__(self, weights):
        self.pre_sums = [weights[0]]
        self.weights = weights
        for i in range(1, len(weights)):
            self.pre_sums.append(self.pre_sums[-1] + weights[i])
   
    def select(self):
        val = random.randint(1, self.pre_sums[-1])
        return self._find_index(val)
        
    def _find_index(self, val):
        left, right = 0, len(self.weights) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.pre_sums[mid - 1] < val <= self.pre_sums[mid]:
                return mid
            elif val > self.pre_sums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        # return self.weights[left]
        return left