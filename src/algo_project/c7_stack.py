def valid_parenthesis_expression(s):
    parenthesis = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for c in s:
        if c in parenthesis:
            stack.append(c)
        else:
            if stack and parenthesis[stack[-1]] == c:
                stack.pop()
            else:
                return False
    return not stack


from collections import deque

def next_largest_number_to_the_right(nums):
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])
    
    return res
            
            


def evaluate_expression(s):
    stack = []
    res = 0
    current_number = 0
    sign = 1
    
    for c in s:
        if c.isalnum():
            current_number = current_number * 10 + int(c)
        elif c == '-' or c == "+":
            res = res + sign * current_number
            current_number = 0
            sign = -1 if c == '-' else 1
        elif c == '(':
            res = res + sign * current_number
            current_number = 0
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif c == ')':
            res = res + sign * current_number
            sign = stack.pop()
            res = stack.pop() + sign * res
            current_number = 0
        else:
            pass
        
    return res + sign * current_number
    

def repeated_removal_of_adjacent_duplicates(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    res = [stack.pop() for _ in range(len(stack))]
    res.reverse()
    return ''.join(res)


from collections import deque

def maximums_of_sliding_window(nums, k):
    left, right = 0, 0
    res = []
    queue = deque()
    for i in range(len(nums)):
        while queue and nums[i] >= queue[-1][1]:
                queue.pop()
        queue.append((i, nums[i]))

        while queue and queue[0][0] < i + 1 - k: # right - q[0] + 1 > k 
            queue.popleft()
        if i >= k - 1:
            res.append(queue[0][1])
    return res
            
