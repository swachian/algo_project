from collections import deque

def valid_parenthesis_expression(s):
    params = {"(": ")", "[": "]", "{": "}"}
    stack = []
    
    for c in s:
        if c in params:
            stack.append(c)
        else:
            if stack and c == params[stack[-1]]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def next_largest_number_to_the_right(nums):
    n = len(nums)
    res = [0] * n
    
    stack = []
    right = n - 1
    
    while right >= 0:
        num = nums[right]
        while stack and stack[-1] <= num:
            stack.pop()
        res[right] = -1 if not stack else stack[-1]
        stack.append(num)
        right -= 1

    return res

def evaluate_expression(s):
    res = 0
    sign = 1
    cur_num = 0
    stack = []
    
    for c in s:
        if c.isdigit():
            cur_num = cur_num * 10 + int(c)
        elif c == "+" or c == "-":
            res += sign * cur_num
            cur_num = 0
            sign = 1 if c == "+" else -1
        elif c == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
            cur_num = 0
        elif c == ")":
            res += sign * cur_num
            cur_num = 0
            sign = stack.pop()
            res = sign * res + stack.pop()
        else:
            pass
    
    res += sign * cur_num
        
    return res 

def repeated_removal_of_adjacent_duplicates(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)



def maximums_of_sliding_window(nums, k):
    queue = deque()
    n = len(nums)
    result = []
    for i, num in enumerate(nums):
        while queue and queue[0][1] < (i+1) - k:
            queue.popleft()
        while queue and queue[-1][0] <= num:
            queue.pop()
        queue.append((num, i))
        if (i + 1) >= k:
            result.append(queue[0][0])
            
    return result

