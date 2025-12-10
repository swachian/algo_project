def substring_anagrams(s, t):
    len_s, len_t = len(s), len(t)
    if len_s < len_t:
        return 0
    
    res = 0
    expected_stats = [0] * 26
    str_stats = [0] * 26
    for c in t:
        expected_stats[ord(c) - ord('a')] += 1
        
    left = right = 0
    while right < len_s:
        str_stats[ord(s[right]) - ord('a')] += 1
        if right - left + 1 == len_t:
            if str_stats == expected_stats:
                res += 1
            str_stats[ord(s[left]) - ord('a')] -= 1
            left += 1
        
        right += 1
        
                    
    return res