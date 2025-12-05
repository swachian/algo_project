def hamming_weights_of_integers(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
        
    return dp

def lonely_integer(nums):
    res = 0
    for num in nums:
        res ^= num
        
    return res

def swap_odd_and_even_bits(n):
    odd_mask = 0xAAAAAAAA
    even_mask = 0x55555555
    result = ((n & odd_mask) >> 1) | ((n & even_mask) << 1)
    return result