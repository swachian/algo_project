import pytest
from algo_project.c5_sliding_window import substring_anagrams, longest_substring_with_unique_chars, longest_uniform_substring_after_replacements


def test_basic_anagrams():
    """
    Test a basic case where s contains multiple substrings
    that are anagrams of t.
    """
    s = "cbaebabacd"
    t = "abc"
    # "cba" (index 0–2) and "bac" (index 6–8) are anagrams of "abc"
    assert substring_anagrams(s, t) == 2

def test_no_anagrams():
    """
    Test a case where s does not contain any substring
    that is an anagram of t.
    """
    s = "abcdefg"
    t = "xyz"
    # No anagrams of "xyz" exist in s
    assert substring_anagrams(s, t) == 0

def test_longest_unique_substring_basic():
    assert longest_substring_with_unique_chars("abcabcbb") == 3  # "abc"
    assert longest_substring_with_unique_chars("bbbbb") == 1      # "b"

def test_longest_unique_substring_edge_cases():
    assert longest_substring_with_unique_chars("") == 0           # empty string
    assert longest_substring_with_unique_chars("pwwkew") == 3     # "wke"
    assert longest_substring_with_unique_chars("abcdef") == 6     # all unique
    
def test_basic_case():
    # 示例：通过替换 2 个字符可以把 "AABABBA" 转为 "AAAAAAA"
    # 最长连续相同子串长度为 5 ("AABBBBA" -> "AAAAA" 之类)
    s = "AABABBA"
    k = 1
    assert longest_uniform_substring_after_replacements(s, k) == 4

def test_all_unique():
    # "ABCDE", k=2 -> 可替换两个字符，例如 "AABCD" 变成 "AAA" 或 "CCC"
    # 最长长度 = 3
    s = "ABCDE"
    k = 2
    assert longest_uniform_substring_after_replacements(s, k) == 3