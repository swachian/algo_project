class SumBetweenRange:
    # init 里预求和，然后在sum_range中，就可以把pre[j] - pre[i - 1]来获得range之间的结果，需要注意i为0的情况
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_nums = [self.nums[0]]
        
        for i in range(1, len(nums)):
            self.pre_nums.append(self.pre_nums[-1] + nums[i])
            

    def sum_range(self, i: int, j: int):
        pre = self.pre_nums[i - 1] if i > 0 else 0
        return self.pre_nums[j] - pre

    
def k_sum_subarrays(nums, k):
    # 定义累计和的hash,0对应的频率为1,表示可以什么数字都不加
    # 遍历数组，更新当前的累计值，如果累计值-k在hash中，则总体feq+上hash中的值，提升当前值在hash中的频率
    prefix_sum_map = {}
    cur_perfix_sum = 0
    prefix_sum_map[cur_perfix_sum] = 1
    count = 0
    
    for num in nums:
        cur_perfix_sum += num
        compliment = cur_perfix_sum - k
        if compliment in prefix_sum_map:
             count += prefix_sum_map[compliment]
        prefix_sum_map[cur_perfix_sum] = 1 if cur_perfix_sum not in prefix_sum_map else prefix_sum_map[cur_perfix_sum] + 1
        
    return count  

def product_array_without_current_element(nums):
    n = len(nums)
    if n == 0:
        return
    res = [1] * n
    pre = nums[0]
    
    for i in range(1, n):
        pre, res[i] = nums[i], pre * res[i - 1]
    
    pre = nums[n - 1]
    for i in range(n - 2, -1, -1):
        res[i], pre = pre * res[i], pre * nums[i]
        
    return res