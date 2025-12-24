def substring_anagrams(s, t):
    if not s or not t:
        return 0
    t_count = [0] * 26
    s_count = [0] * 26

    for c in t:
        t_count[ord(c) - ord('a')] += 1
    
    left = right = 0
    sub_count = 0
    while right < len(s):
        s_count[ord(s[right]) - ord('a')] += 1
        if right - left + 1 == len(t):
            if s_count == t_count:
                sub_count += 1
            s_count[ord(s[left]) - ord('a')] -= 1
            left += 1
        right += 1
    return sub_count
        
            
        
        

 

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
