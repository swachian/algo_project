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

def gas_stations(gas, cost):
    # 先用gas的总和和cost的总和进行对比，只要gas总和大于等于cost,就总有解
    # 然后，从0开始，迭代尝试tank里是否有剩余，如果没有则从断点之后继续进行，直到某个点可以走到数组尾部
    
    if sum(gas) < sum(cost):
        return -1
    
    start, tank = 0, 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start

def candies(ratings):
    # 也是两道遍历的方法
    # xxxix先给所有的候选者配备1, 之后第一遍从左到右发现有上升就多分一个，最后第二遍从右到左，发现分数高的就多加一个
    # 从右往左比较的时候，需要注意比较候选者的条件
    n = len(ratings)
    cadidates = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            cadidates[i] = cadidates[i - 1] + 1
            
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and cadidates[i] <= cadidates[i + 1]:
            cadidates[i] = cadidates[i + 1] + 1
    return sum(cadidates)