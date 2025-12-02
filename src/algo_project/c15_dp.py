memo = {}

def climbing_stairs(n):
    if n <= 2:
        return n
    
    if n in memo:
        return memo[n]
    result = climbing_stairs(n - 2) + climbing_stairs(n - 1)
    memo[n] = result
    return memo[n]


def min_coin_combination(coins, target):
    # 可以有top down和bottom up两种方式，前者是递归，后者是dp
    # base cases: target = 0 => count = 0
    # recurrence solution: min(min_value, 1 + top_down(coins, target - coin))
    # 后者是子问题的最优解
    
    # bottom up 就翻译一下，要点也是base cases和recurrence
    result = bottom_up_min_coin_combination(coins, target) #top_down_min_coin_combination(coins, target)
    return result if result != float("inf") else -1

def top_down_min_coin_combination(coins, target, memo = {}):
    if target == 0:
        return 0
    if target in memo:
        return memo[target]
    
    count = float("inf")
    for coin in coins: 
        if coin <= target:
            count = min(count, 1 + top_down_min_coin_combination(coins, target - coin, memo))
            
    memo[target] = count
    return count

def bottom_up_min_coin_combination(coins, target):
    dp = [float("inf")] * (target + 1)
    dp[0] = 0
    for sub_target in range(target + 1):
        for coin in coins:
            if coin <= sub_target:
                dp[sub_target] = min(dp[sub_target], 1 + dp[sub_target - coin])
    return dp[target]

def matrix_pathways(m, n):
    # base cases: r0和c0的次数都是1
    # recurrence solution: dp[r-1][col] + dp[r][col - 1]
    # 特例，只要用两个row就能d裁剪到上面的dp
    prev_row = [1] * n
    for r in range(1, m):
        cur_row = [1] * n
        for c in range(1, n):
            cur_row[c] = cur_row[c - 1] + prev_row[c]
        prev_row = cur_row
    return prev_row[n - 1]