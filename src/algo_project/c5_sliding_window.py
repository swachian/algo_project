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

    