def substring_anagrams(s, t):
    if not s and not t:
        return True
    
    s_array = [0] * 26
    t_array = [0] * 26
    count = 0
    
    for c in t:
        t_array[ord(c) - ord('a')] += 1
    
    left = right = 0
    while right < len(s):
        c = s[right]
        s_array[ord(c) - ord('a')] += 1
        if right - left + 1 == len(t):
            if s_array == t_array:
                count += 1
            c = s[left]
            left += 1
            s_array[ord(c) - ord('a')] -= 1
        right += 1
    return count

        
            
        
        

from collections import defaultdict

def longest_substring_with_unique_chars(s):
    num_maps = {}

    left, right = 0, 0
    max_len = 0
    while right < len(s):
        if s[right] in num_maps:
            pass
            # move left point
            while s[left] != s[right]:
                del num_maps[s[left]]
                left += 1
            del num_maps[s[left]]    
            left += 1
        num_maps[s[right]] = right
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len

from collections import defaultdict

def longest_uniform_substring_after_replacements(s, k):
    chars_count = defaultdict(int)
    left = right = 0
    max_count = 0
    
    while right < len(s):
        chars_count[s[right]] += 1
        max_count = max(max_count, chars_count[s[right]])
        if right - left + 1 - max_count > k:
            chars_count[s[left]] -= 1
            left += 1
        right += 1
        
    return right - left
