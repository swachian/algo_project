def jump_to_the_end(nums):
    # base: dp[0] = True if nums[0] != 0
    # recurrence solution: dp[i] = num + i
    
    # algorithm in the book
    # 从最右面开始，每次只找到最低的满足可以跳过来的destination,并设置为新的destination
    # 结果判断destination是否可达起点0
    destination = len(nums) - 1
    for i in range(destination, -1, -1):
        if nums[i] + i >= destination:
            destination = i
    return destination == 0