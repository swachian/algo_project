def jump_to_the_end(nums):
    destination = len(nums) - 1

    for i in range(destination, -1, -1):
        if i + nums[i] >= destination:
            destination = i
    return destination == 0

def gas_stations(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    start = 0
    tank = 0
    for i in range(start, len(gas)):
        tank += gas[i]
        tank -= cost[i]

        if tank < 0:
            start = i + 1
            tank = 0
            
    return start