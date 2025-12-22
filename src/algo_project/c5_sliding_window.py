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

def longest_substring_with_unique_chars(s):
    char_map = {}
    left = right = 0
    res = 0
    
    while right < len(s):
        if s[right] in char_map:
            last_occurence = char_map[s[right]]
            while left <= last_occurence:
                del char_map[s[left]]
                left += 1
        res = max(res, right - left + 1)
        char_map[s[right]] = right 
        right += 1
    
    return res

from collections import defaultdict

def longest_uniform_substring_after_replacements(s, k):
    freq = defaultdict(int)
    max_freq = 0
    left = 0
    right = 0
    
    while right < len(s):
        freq[s[right]] += 1
        max_freq = max(max_freq, freq[s[right]])
        sub_length = right - left + 1
        if sub_length - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        right += 1
        
    return right - left
