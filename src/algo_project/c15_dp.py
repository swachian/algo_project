def climbing_stairs(n):
    # base: dp[1] = 1, dp[2] = 2
    # rs: dp[i] = dp[i - 1] + dp[i - 2]
    if n <= 2:
        return n
    prev = 2
    prev_prev = 1
    for i in range(3, n + 1):
        next_stairs = prev + prev_prev
        prev_prev = prev
        prev = next_stairs
    return next_stairs


def min_coin_combination(coins, target):
    # base: dp[0] =  0
    # rs: dp[i] = min(dp[i - coin] + 1)
    dp = [float("inf")] * (target + 1)
    dp[0] = 0
    for i in range(target + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != float("inf"):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[target] if dp[target] != float("inf") else -1


def matrix_pathways(m, n):
    # base: prev = [1....], cur = [1]
    # cur[i] = prev[i] + cur[i]
    prev = [1] * n
    for i in range(1, m):
        cur = [1] * n
        for j in range(1, n):
            cur[j] = prev[j] + cur[j - 1]
        prev = cur
    return prev[-1]


def neighborhood_burglary(houses):
    # base: dp[0] = houses[0], dp[1] = max(dp[0], houses[1])
    # recurrence solution: dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    if not houses:
        return 0
    if len(houses) <= 1:
        return houses[0]


    prev_value = houses[0]
    current_value = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        next_value = max(prev_value + houses[i], current_value)
        prev_value = current_value
        current_value = next_value
    return current_value

def longest_common_subsequence(s1, s2):
    # base: dp[0][x] = 0, dp[x][0] = 0
    # rs: if s1[i - 1] == s2[j - 1] dp[i][j] = 1 + dp[i - 1][j - 1]
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    count = 0
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

                
    return dp[m][n]


def longest_palindrome_in_a_string(s):
    # base: dp[i][i] = 1 , dp[i][i + 1] = 2 if s[i] == s[i] + 1
    # rs:dp[i - 1][j + 1] = dp[i][j] + 2 if s[i - 1] == s[j + 1] and dp[i][j] > 0
    if not s:
        return 0
    n = len(s)
    dp = [[0] * n for _ in range(n) ]
    res_i, res_j = 0, 0
    for i in range(n):
        dp[i][i] = 1
    for i in range(0, n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 2
            res_i, res_j = i, i + 1
            
    for sub_len in range(3, n + 1):
        for i in range(n + 1 - sub_len):
            j = sub_len + i - 1
            if s[i] == s[j] and dp[i + 1][j - 1] > 0:
                dp[i][j] = dp[i + 1][j - 1] + 2
                res_i, res_j = i, j
    return s[res_i:res_j + 1]
    
    
    

def maximum_subarray_sum(nums):
    #base: dp[0] = nums[0]
    #rs: dp[i] = max(dp[i - 1] + nums[i], nums[i])
    if not nums:
        return 0
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
    return max(dp)

        
def knapsack(k, weights, values):
    # base: dp[m + 1][n + 1], dp[0][*] = 0, dp[*][0] = 0
    # recurrence solution: load or unload dp[i][c] = max(values[i - 1] + dp[i-1][c - weight], dp[i-1][c])
    m = len(weights)
    dp = [[0] * (k + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, k + 1):
            if j - weights[i - 1] >= 0:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j - 1])
            else:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][k]
    
    
def largest_square_in_a_matrix(matrix):
    # base: dp[0][x] = 1 if matrix[0][x] == 1, dp[x][0] = 1 if matrix[x][0] == 1
    # if matrix[i][j] == 1, dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]])
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    max_count = 0
    dp = [[0] * n for _ in range(m)]

    for j in range(n):
        if matrix[0][j] == 1:
            dp[0][j] = 1
            max_count = 1
    
    for i in range(m):
        if matrix[i][0] == 1:
            dp[i][0] = 1
            max_count = 1
            
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j])
                max_count = max(max_count, dp[i][j])
    
    
    return max_count ** 2