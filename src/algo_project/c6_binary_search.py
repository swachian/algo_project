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

    left = find_left_lower(nums, target)
    right = find_right_upper(nums, target)
    return [left, right]

def find_left_lower(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if nums[left] == target else -1



def find_right_upper(nums, target):
    left, right = 0, len(nums) - 1
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
    half_size = (m + n) // 2
    
    left, right = 0, m - 1
    while True:
        mid = left + (right - left) // 2
        mid2 = half_size - mid - 2
        L1 = nums1[mid] if 0 <= mid < m else float("-inf")
        R1 = nums1[mid + 1] if -1 <= mid < m - 1 else float("inf")
        L2 = nums2[mid2] if 0 <= mid2 < n else float("-inf")
        R2 = nums2[mid2 + 1] if -1 <= mid2 < n - 1 else float("inf")
        
        if L1 > R2:
            right = mid - 1
        elif L2 > R1:
            left = mid + 1
        else:
            if (m + n) % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2
            else:
                return min(R1, R2) 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
def matrix_search(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])

    left, right = 0, m * n - 1
    while left <= right:
        mid = left + (right - left) // 2
        i, j = mid // n, mid % n
        c = matrix[i][j]
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            left = mid + 1
        else:
            right = mid - 1
    return matrix[i][j] == target
            
            
            
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
        num = random.randint(1, self.pre_sums[-1])
        left = 0
        right = len(self.pre_sums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if num <= self.pre_sums[mid]:
                if mid == 0:
                    return mid
                elif num > self.pre_sums[mid - 1]:
                    return mid 
                else:
                    right = mid - 1
            else:
                left = mid + 1
        return left
                    
                

