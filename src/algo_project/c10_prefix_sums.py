class SumBetweenRange:
    def __init__(self, nums):
        self.pre_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.pre_sum.append(self.pre_sum[-1] + nums[i])
    
    def sum_range(self, i, j):
        pre = self.pre_sum[i - 1] if i > 0 else 0
        return self.pre_sum[j] - pre
  
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
    
    right_product = nums[n - 1]
    for i in range(n - 2, -1, -1):
        res[i] = res[i] * right_product
        right_product *= nums[i] 
    
    return res
