def spiral_matrix(matrix):
    #  设置top, bottom， left, right 4个边界，只要top和left没有越过bottom和right,就持续遍历
    # 中间第三和第四步时，因为top和right已经做过修正，所以要再次判断top或right是否已经越过bottom和left
    if not matrix:
        return []
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    res = []
    
    while top <= bottom and left <= right:
        i = top
        j = left
        for j in range(left, right + 1):
            res.append(matrix[i][j])
        top += 1
        
        for i in range(top, bottom + 1):
            res.append(matrix[i][j])
        right -= 1
        
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[i][j])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][j])
            left += 1
        
    return res

import math
        
def reverse_32_bit_integer(n):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    reverse_n = 0
    
    while n != 0:
        if reverse_n > INT_MAX / 10 or reverse_n < INT_MIN / 10:
            return 0
        digit = int(math.fmod(n, 10))
        reverse_n = 10 * reverse_n + digit

        n = int(n / 10)
    return reverse_n

from collections import defaultdict

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def maximum_collinear_points(points):
    res = 0
    for focus in points:
        res = max(res, count_slope(focus, points))
    return res

def count_slope(focus, points):
    counters = defaultdict(int)
    max_count = 0
    for point in points:
        if point == focus:
            continue
        slope = compute_slope(focus, point)
        counters[slope] += 1
        max_count = max(max_count, counters[slope])
    return max_count + 1

def compute_slope(focus, point):
    rise = point[1] - focus[1]
    run = point[0] - focus[0]
    
    if run == 0:
        return (float("inf"), run)
    else:
        a = gcd(rise, run)
        return (rise // a, run // a)
    
def josephus1(n, k):
    people = [i + 1 for i in range(n)]
    remove = 0

    i = 0
    last = 0
    while remove < n - 1:
        count = 0
        while count < k:
            if people[i] == 0:
                i = (i + 1) % n
                continue
            else:
                count += 1
                last = i
                i = (i + 1) % n
                
            
        remove += 1
        people[last] = 0
        
        
        
    return max(people) - 1

def josephus2(n, k):
    # base: dp[0] = 0, dp[1] = 0
    # recurrence solution: dp[i] = (dp[i - 1] + k) % i
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] + k) % i
    return dp[n]

def josephus3(n, k):
    if n == 0 or n == 1:
        return 0
    return (k + josephus3(n - 1, k)) % n