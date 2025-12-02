def climbing_stairs(n):
    if n <= 2:
        return n
    
    one_step_before, two_step_before = 2, 1
    current_step = 0
    for i in range(3, n + 1):
        current_step = one_step_before + two_step_before
        two_step_before = one_step_before
        one_step_before = current_step
    
    return one_step_before