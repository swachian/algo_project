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
    presum_hash = defaultdict(int)
    presum_hash[0] = 1
    
    count = 0
    presum = 0
    for i in range(len(nums)):
        presum += nums[i]
        complement = presum - k
        if complement in presum_hash:
            count += presum_hash[complement] 
        presum_hash[presum] += 1
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
