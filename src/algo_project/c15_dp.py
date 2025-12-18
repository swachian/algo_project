def climbing_stairs(n):
    if n <= 2:
        return n
    two_step_before = 1
    one_step_before = 2
    current_step = 0
    for i in range(3, n + 1):
        current_step = one_step_before + two_step_before
        two_step_before = one_step_before
        one_step_before = current_step
    
    return current_step


def min_coin_combination(coins, target):
    # base: dp[0] = 0, 
    # recurrence solution: dp[i] = min(coin + dp[i-coin]) for coin in coins
    dp = [-1] * (target + 1)
    dp[0] = 0
    
    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != -1:
                dp[i] = min(dp[i], dp[i - coin] + 1) if dp[i] != -1 else dp[i - coin] + 1
    return dp[target]


def matrix_pathways(m, n):
    # base: dp[0][*] = 1, dp[*][0] = 1
    # recurrence solution: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    cur_row = prev_row = [1] * n
    for i in range(1, m):
        cur_row = [1] * n
        for j in range(1, n):
            cur_row[j] = prev_row[j] + cur_row[j - 1]
        prev_row = cur_row
    return cur_row[n - 1]