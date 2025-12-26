def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    
    top, bottom = 0, len(matrix) 
    left, right = 0, len(matrix[0])
    res = []
    
    while top < bottom and left < right:
        i = top
        for j in range(left, right):
            res.append(matrix[i][j])
        top += 1
        
        for i in range(top, bottom):
            res.append(matrix[i][j])
        right -= 1
        
        if top < bottom:
            for j in range(right - 1, left - 1, -1):
                res.append(matrix[i][j])
            bottom -= 1
        
        if left < right:
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][j])
        left += 1
    return res


import math
def reverse_32_bit_integer(n):
    MIN_INT = - 2 ** 32
    MAX_INT = 2 ** 32 - 1
    
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    
    res = 0
    while n > 0:
        if res >= MAX_INT / 10:
            return 0
        digit = n % 10
        res = res * 10 + digit
        n = int(n / 10)
    return sign * res
  
  
from collections import defaultdict
 
def maximum_collinear_points(points):
    max_count = 0
    for focus in points:
        count = collinear_points_of_focus(focus, points)
        max_count = max(max_count, count)  
    return max_count

def gcd(x, y):
    while y != 0:
        x, y = y, x % y  
    return x
  
def compute_slope(p1, p2):
    rise = p2[1] - p1[1]  
    span = p2[0] - p1[0]

    gcd_num = gcd(rise, span)
    if gcd_num == 0:
        return ((float("inf"), 0))
    else:
        return (rise // gcd_num, span // gcd_num)
  
def collinear_points_of_focus(focus, points):
    max_count = 0
    counts = defaultdict(int)
    for point in points:
        if point == focus:
            continue
        slope = compute_slope(focus, point)
        counts[slope] += 1
        max_count = max(max_count, counts[slope])
    return max_count + 1
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


def josephus1(n, k):
    # base: dp[1] = 0
    # rs: dp[i] = (dp[i - 1] + k) % i
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + k) % i
    return dp[n]


def triangle_numbers(n):
    if n % 2 == 1:
        return 2
    if n %4 == 0:
        return 3
    else:
        return 4