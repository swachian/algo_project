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
    cur_num = 0
    sign = 1
    res = 0
    for c in s:
        if c.isdigit():
            cur_num = cur_num * 10 + int(c)
        elif c == '-' or c == '+':
            res += sign * cur_num
            sign = 1 if c == '+' else -1
            cur_num = 0
        elif c == '(':
            res += cur_num * sign
            stack.append(res)
            stack.append(sign)
            cur_num = 0
            sign = 1
            res = 0
        elif c == ')':
            res += sign * cur_num
            cur_num = 0
            sign = stack.pop()
            res = sign * res + stack.pop()
        else:
            pass
    res += cur_num * sign
    return res

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
    queue = deque()
    res = []
    for i in range(len(nums)):
        while queue and  queue[0][1] < i - k + 1:
            queue.popleft()
        while queue and queue[-1][0] <= nums[i]:
            queue.pop()
        queue.append((nums[i], i))
        if i + 1 >= k:
            res.append(queue[0][0])
    return res