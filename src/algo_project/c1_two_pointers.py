def pair_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    res = []
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s > target:
            right -= 1
        else:
            left += 1
            
    return res

    
def triplet_sum(nums):
    nums.sort()
    res = []

    for i, num in enumerate(nums):
        if i > 0 and nums[i - 1] == num:
            continue
        pairs = pairs_sum(nums, i + 1, 0 - num)
        for b, c in pairs:
            res.append([num, nums[b], nums[c]])
    return res
    
def pairs_sum(nums, i, target):
    res = []
    left, right = i, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            res.append((left, right))
            left += 1
            while nums[left] == nums[left - 1] and left < right:
                left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
    return res


        
def find_pairs_sum(nums, start, target):
    res = []
    left = start
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            res.append([nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
    return res
        
def is_palindrome_valid(s):
    left, right = 0, len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1       
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right = -1
    return True


def largest_container(heights):
    left, right = 0, len(heights) - 1
    max_vol = 0
    while left < right:
        max_vol = max(max_vol, min(heights[right], heights[left]) * (right - left))
        if heights[left] > heights[right]:
            right -= 1
        elif heights[left] < heights[right]:
            left += 1
        else:
            left += 1
            right -= 1
    return max_vol

def shift_zeros_to_the_end(nums):
    zero_p = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_p], nums[i] = nums[i], nums[zero_p]
            zero_p += 1
    return nums


def next_lexicographical_sequence(s):
    # 1. 从右往左，找到第一个下降的pair
    # 2. 记录下小的值
    # 3. 继续从右往左，找到第一个大于前面的小值的值，并进行swap
    # 4. 对swap后的子串进行reverse并拼接回去
    slist  = list(s)
    right = len(s) - 1
    pov = -1
    while right > 0:
        if slist[right] > slist[right - 1]:
            pov = right - 1
            break
        else:
            right -= 1
    if pov < 0:
        return s[::-1]
    
    right = len(s) - 1
    while right > pov:
        if slist[right] > slist[pov]:
            break
        else:
            right -= 1
    slist[pov], slist[right] = slist[right], slist[pov]
    ss = slist[0:pov + 1] + slist[pov + 1:][::-1]
    return "".join(ss)
        
        
