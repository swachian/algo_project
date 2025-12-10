chars_count = {}
t_chars_count = {}

def substring_anagrams(s, t):
    left = right = 0
    n = len(s)
    tn = len(t)
    count = 0
    for c in t:
        t_chars_count[c] = t_chars_count.get(c, 0) + 1
        
    while right < n:
        chars_count[s[right]] = chars_count.get(s[right], 0) + 1
        if right - left + 1 == tn:
            if compare_maps():
                count += 1
            chars_count[s[left]] -= 1
            left += 1
            
        right += 1
    return count
    
def compare_maps():
    for key in t_chars_count.keys():
        if key in chars_count and chars_count[key] == t_chars_count[key]:
            continue
        else:
            return False
    return True

def longest_substring_with_unique_chars(s):
    left = right = 0
    n = len(s)
    hash = {}
    count = 0
    while right < n:
        while s[right] in hash:
            c = s[left]
            del hash[c]
            left += 1
        count = max(count, right - left + 1)
        hash[s[right]] = hash.get(s[right], 0) + 1
        right += 1
    return count
    
def is_unique_chars(hash, c):
    return c in hash    
    
def longest_uniform_substring_after_replacements(s, k):
    # 动态窗口的算法
    # 记录下某个动态窗口下同一个字符的最大频率，如果窗口减去该最大频率后大于k，则缩小窗口并重新寻找新的最高频率
    left = right = 0
    n = len(s)
    hash = {}
    highest_freq = 0
    window_len = 0
    
    while right < n:
        c = s[right]
        hash[c] = hash.get(c, 0) + 1
        highest_freq = max(highest_freq, hash[c])
        window_len = right - left + 1
        if (window_len - highest_freq > k):
            c = s[left]
            hash[c] -= 1
            left += 1
        window_len = right - left + 1
        right += 1 
    return window_len 