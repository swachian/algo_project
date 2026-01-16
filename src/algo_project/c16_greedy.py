def jump_to_the_end(nums):
    right = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] + i >= right:
            right = i
    return right == 0


 


def gas_stations(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    i = 0
    start = i
    tank = 0
    while i < len(gas):
        tank += gas[i]
        tank -= cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
        i += 1
        
    return start
        


def candies(ratings):
    if not ratings:
        return 0
    
    n = len(ratings)
    res = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            res[i] = res[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
            res[i] = res[i + 1] + 1
    
    return sum(res)
        

        
