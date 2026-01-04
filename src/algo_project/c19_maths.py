def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return matrix
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    res = []

    while top <= bottom and left <= right:
        i = top
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
    MAX_INT = 2 ** 32 - 1
    sign = 1
    if n < 0:
        n *= -1
        sign = -1
    val = 0
    while n > 0:
        if val > MAX_INT // 10:
            return 0
        digital = n % 10
        val = val * 10 + digital
        n = n // 10
    return sign * val

  
from collections import defaultdict
 
def maximum_collinear_points(points):
    max_count = 0
    for focus in points:
        focus_count = count_for_one_point(focus, points)
        max_count = max(max_count, focus_count)
    return max_count

def compute_slope(p1, p2):
    rise = p1[1] - p2[1]
    span = p1[0] - p2[0]

    if span != 0:
        gcd_number = gcd(rise, span)

        return (rise // gcd_number, span // gcd_number)
    else:
        return (float("inf"), 0)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def count_for_one_point(focus, points):
    slope_maps = defaultdict(int)
    max_count = 0
    for point in points:
        if point == focus:
            continue
        slope = compute_slope(focus, point)
        slope_maps[slope] += 1
        max_count = max(max_count, slope_maps[slope])
    return max_count + 1
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


def josephus1(n, k):
    # base: dp[1] = 0
    # rs: dp[i] = (dp[i - 1] + k) % i
    if n <= 1:
        return 0
    return (josephus1(n - 1, k) + k) % n


def triangle_numbers(n):
    if n % 2 == 1:
        return 2
    elif n % 4 == 0:
        return 3
    else:
        return 4