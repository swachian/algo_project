def spiral_matrix(matrix):
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
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31
    
    res = 0
    sign = 1
    if n < 0:
        sign = -1
        
    while n != 0:
        if res > MAX_INT / 10 or res < MIN_INT / 10:
            return 0
        dig = n % (sign * 10)
        n = int(n / 10)
        res = res * 10 + dig

    return res

from collections import defaultdict

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def maximum_collinear_points(points):
    max_counts = 0
    for focus in points:
        max_counts = max(max_counts, max_points_of_every_focus(focus, points))
    return max_counts

def max_points_of_every_focus(focus, points):
    same_slope_counts_of_a_point = defaultdict(int)
    max_points = 0
    for point in points:
        if point == focus:
            continue
        slope = compute_slope(focus, point)
        same_slope_counts_of_a_point[slope] += 1
        
        max_points = max(max_points, same_slope_counts_of_a_point[slope])
            
    return max_points + 1
             

def compute_slope(p1, p2):
    rise = p2[1] - p1[1]
    span = p2[0] - p1[0]
    
    if span == 0:
        return (1, 0)
    gcd_number = gcd(rise, span)
    return (rise // gcd_number, span // gcd_number)

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