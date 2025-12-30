class SumBetweenRange:
    def __init__(self, nums):
        self.nums = nums
        self.pre_sums = [nums[0]]
        for i in range(1, len(nums)):
            self.pre_sums.append(self.pre_sums[-1] + nums[i])

    def sum_range(self, i, j):
        pre = 0 if i == 0 else self.pre_sums[i - 1]
        return self.pre_sums[j] - pre
 
  
from collections import defaultdict  
def k_sum_subarrays(nums, k):
    pre_sum_map = defaultdict(int)

    pre_sum_map[0] = 1
    count = 0
    pre_sum = 0
    for num in nums:
        pre_sum += num
        complement = pre_sum - k
        if complement in pre_sum_map:
            count += pre_sum_map[complement]
        pre_sum_map[pre_sum] += 1
    return count

      
      

        

def product_array_without_current_element(nums):
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    
    pre = nums[n - 1]
    for i in range(n - 2, -1, -1):
        res[i] = res[i] * pre 
        pre = pre * nums[i]
    
    return res
