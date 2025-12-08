def pair_sum_sorted(nums, target):
    i = 0
    j = len(nums) - 1
    while j > i:
        sum = nums[i] + nums[j]
        if sum > target:
            j -=1 
        elif sum < target:
            i += 1
        else:
            return [i, j]
        
    return []

def triplet_sum(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    i = 0
    result = []
    a = None
    while i < n - 2:
        if a == sorted_nums[i]:
            i += 1
            continue
        a = sorted_nums[i]
        if a > 0:
            break
        
        j = i + 1
        k = n - 1
        while k > j:
            b = sorted_nums[j]
            sum = sorted_nums[j] + sorted_nums[k]
            if sum == -a:
                result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                j += 1
                while b == sorted_nums[j] and j < k:
                    j += 1
            elif sum < -a:
                j += 1
            else:
                k -= 1
                
    return result
    
    
def is_palindrome_valid(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

def largest_container(heights):
    i, j = 0, len(heights) - 1
    # if j < 1:
    #     return 0
    max_result = 0
    while j > i:
        max_result = max(max_result, (j - i) * min(heights[i], heights[j]))
        if heights[i] == heights[j]:
            i += 1
            j -= 1
        elif heights[i] > heights[j]:
            j -= 1
        else:
            i += 1
            
    return max_result

def shift_zeros_to_the_end(nums):
    left = 0
    # Iterate through the array using a 'right' pointer to locate non-zero
    # elements.
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            # Increment 'left' since it now points to a position already occupied
            # by a non-zero element.
            left += 1
    return nums

def next_lexicographical_sequence(s):
    n = len(s)
    j = n - 1
    pov = -1
    while j > 0:
        if s[j] > s[j - 1]:
            pov = j - 1
            break
        j -= 1
    
    if pov == -1:
        return s[::-1]
    
    c = s[pov]
    chars = list(s)
    j = n - 1
    while j > pov:
        if s[j] > c:
            chars[j], chars[pov] = chars[pov], chars[j]
            break
        j -= 1
    return "".join(chars[0:pov+1] + chars[pov+1:][::-1])
    # return ''.join(chars)