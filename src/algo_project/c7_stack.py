from collections import deque

def valid_parenthesis_expression(s):
    # 这个比较简单，技巧在于判断key在不在map里，以及栈顶的元素能不能凑成一对
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
    # 从右边开始遍历，同时使用一个栈，弹出栈里面所有小于当前指向的元素，如栈还不为空，则栈顶元素即res中的一个
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
    # 对表达式中的4种符号类型进行不同的处理，同时将res和sign存入栈中。
    # 遇到数字，则把curnum不断进位，遇到符号，表明可以进行res的处理并修改sign的直
    # 遇到左括号，把res和sign入栈，然后清零，遇到右括号，完成当前res sign和num的计算，并弹出之前的sign和res进行加减
    
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
    # 不停和栈顶元素对比，如果相等，则抵消否则入栈
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)



def maximums_of_sliding_window(nums, k):
    # 利用队列，队列记录（元素， 索引）的元组，遍历数组，在队列左边把所有过期的索引的元素都弹出，
    # 右边则把小于当前元素的的元素都去除，把当前元素加入队列，则队列头就是当前最大的元素
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

