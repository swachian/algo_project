def valid_parenthesis_expression(s):
    parentheses = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for c in s:
        if c in parentheses:
            stack.append(c)
        else:
            if not stack or c != parentheses[stack[-1] ]:
                return False
            stack.pop()
    return not stack

from collections import deque

def next_largest_number_to_the_right(nums):
    stack = []
    res = [-1] * len(nums)
    
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res

def evaluate_expression(s):
    stack = []
    cur_number = 0
    sign = 1
    res = 0
    
    for c in s:
        if c.isdigit():
            cur_number = cur_number * 10 + int(c)
        elif c == '-' or c == '+':
            res += sign * cur_number
            cur_number = 0
            sign = -1 if c == '-' else 1
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif c== ')':
            res += sign * cur_number
            sign = stack.pop()
            res = stack.pop() + sign * res
            cur_number = 0
        else:
            pass
    return res + sign * cur_number

def repeated_removal_of_adjacent_duplicates(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

from collections import deque

def maximums_of_sliding_window(nums, k):
    queue = deque()
    res = []
    
    for i, num in enumerate(nums):
        while queue and queue[0][0] < i + 1 - k:
            queue.popleft()
        while queue and queue[-1][1] <= num:
            queue.pop()
        queue.append((i, num))
        if i >= k - 1:
            res.append(queue[0][1])
    return res