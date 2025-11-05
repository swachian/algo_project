import pytest
from algo_project.c5_sliding_window import substring_anagrams


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
