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
    for i in range(0, len(nums) - 2):
        target = - nums[i]
        if i >= 1 and nums[i - 1] == nums[i]:
            continue
        pair = pair_sum_for_triplet(nums, i + 1, len(nums) - 1, target)
        if pair:
            for b, c in pair:
                res.append([nums[i], nums[b], nums[c]])
    return res
    
def pair_sum_for_triplet(nums, i, j, target):
    res = []
    while i < j:
        s = nums[i] + nums[j]
        if s > target:
            j -= 1
        elif s < target:
            i += 1
        else:
            res.append([i, j])
            i += 1
            j -= 1
            while i < j and nums[i] == nums[i - 1]:
                i += 1
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
    left = 0
    right = len(heights) - 1
    largest = 0
    while left < right:
        height = min(heights[left], heights[right])
        largest = max(largest, (right - left) * height)
        if heights[left] > heights[right]:
            right -= 1
        elif heights[right] > heights[left]:
            left += 1
        else:
            left += 1
            right -= 1
    return largest

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
        
        
