def jump_to_the_end(nums):
    # base: dp[0] = True if nums[0] != 0
    # recurrence solution: dp[i] = num + i
    if not nums:
        return False
    dp = [False] * len(nums)
    if nums[0] > 0:
        if nums[0] >= len(nums):
            return True
        for i in range(nums[0] + 1):
            dp[i] = True
    for i in range(1, len(nums)):
        if not dp[i]:
            return False
        else:
            for cavort in range(nums[i] + 1):
                if i + cavort >= len(nums):
                    return True
                dp[i + cavort] = True
    return True