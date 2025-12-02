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

def neighborhood_burglary(houses):
    # base cases, dp[0] = houses[0]，但这里需要两个base, dp[1] = max(houses[0], houses[1])
    # recurrence solution: dp[i] = max(houses[i] + dp[i - 2], dp[i - 1])
    # 空间优化，只要保留最近两个dp即可
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    prev_prev_max_profit = houses[0]
    prev_max_profit = max(houses[0], houses[1])
    for i in range(2, len(houses)):
        profit = max(prev_prev_max_profit + houses[i], prev_max_profit)
        prev_prev_max_profit = prev_max_profit
        prev_max_profit = profit
    return prev_max_profit


# +-----------------------+-----------------------+
# |        dp[i][j]       |      dp[i][j+1]       |
# |                       |           ←           |
# |           ↑           |        (from right)   |
# |       (from down)     |                       |
# +-----------------------+-----------------------+
# |     dp[i+1][j]        |    dp[i+1][j+1]       |
# |           ↑           |                       |
# |         (diag ↖) <----------------------------|
# |                       |                       |
# +-----------------------+-----------------------+

def longest_common_subsequence(s1, s2):
    # base: 最右面和最下面两个多出来的dp为0
    # recurrence solution: 如果s1[i] == s2[j], dp[i][j]等于右下斜对角的数字+1
    # 否则，取右和下面更大的值
    m, n = len(s1), len(s2)
    prev_row = [0] * (n + 1)
    for i in range(m - 1, -1, -1):
        cur_row = [0] * (n + 1)
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                cur_row[j] = prev_row[j + 1] + 1
            else:
                cur_row[j] = max(cur_row[j + 1], prev_row[j])
        prev_row = cur_row
    return prev_row[0]

def longest_palindrome_in_a_string(s):
    # base: 长度为1的字符dp值为True, 长度为2的字符且左右相等的为True
    # recurrence solution: 这个东西依赖的是左下角，即s[i] == s[j] 且 dp[i+1][j-1]为True是为True
    # 所以实际通过变长的substr来确定不同的i和j的值
    n = len(s)
    dp = [[False] * n for _ in range(n) ]
    
    start_at = 0
    max_length = 0
    for i in range(n):
        dp[i][i] = True
        start_at = i
        max_length = 1
    
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start_at = i
            max_length = 2
    
    for substringlen in range(3, n + 1):
        for i in range(n - substringlen + 1):
            j = i + substringlen - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if substringlen > max_length:
                    max_length = substringlen
                    start_at = i
                    
    return s[start_at:start_at + max_length]