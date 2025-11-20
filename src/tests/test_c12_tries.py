import pytest
from algo_project.c12_tries import Trie, InsertAndSearchWordsWithWildcards, find_all_words_on_a_board


import pytest

# Test 1: Insertion and Search in the Trie
def test_insert_search():
    trie = Trie()
    
    # Insert words into the trie
    trie.insert("apple")
    trie.insert("app")
    
    # Search for words
    assert trie.search("apple") == True  # "apple" is in the trie
    assert trie.search("app") == True    # "app" is in the trie
    assert trie.search("appl") == False  # "appl" is not in the trie
    assert trie.search("banana") == False  # "banana" is not in the trie

# Test 2: Prefix Checking in the Trie
def test_has_prefix():
    trie = Trie()
    
    # Insert words into the trie
    trie.insert("apple")
    trie.insert("app")
    
    # Check for prefixes
    assert trie.has_prefix("app") == True  # "app" is a prefix of "apple" and "app"
    assert trie.has_prefix("ap") == True   # "ap" is a prefix of "apple" and "app"
    assert trie.has_prefix("a") == True    # "a" is a prefix of "apple" and "app"
    assert trie.has_prefix("ban") == False  # "ban" is not a prefix of any word in the trie
    
    
# Test 1: Insert and search words with wildcards
def test_insert_search_with_wildcards():
    trie = InsertAndSearchWordsWithWildcards()
    
    # Insert words into the trie
    trie.insert("bad")
    trie.insert("dad")
    trie.insert("mad")
    
    # Search for words
    assert trie.search("pad") == False   # "pad" is not in the trie
    assert trie.search("bad") == True    # "bad" is in the trie
    assert trie.search(".ad") == True    # ".ad" matches "bad", "dad", "mad"
    assert trie.search("b..") == True    # "b.." matches "bad"
    assert trie.search("ma.") == True    # "ma." matches "mad"
    assert trie.search("b.a") == False    # "b.a" matches "bad"

# Test 2: Search with multiple wildcards and edge cases
def test_search_multiple_wildcards():
    trie = InsertAndSearchWordsWithWildcards()
    
    # Insert words into the trie
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("grape")
    
    # Search for words with wildcards
    assert trie.search("a..le") == True  # "a..le" matches "apple"
    assert trie.search("b.n.n.") == True # "b.n.n." matches "banana"
    assert trie.search("gr.pe") == True  # "gr.pe" matches "grape"
    assert trie.search("..p..") == True  # "..p.." matches "apple" and "grape"
    assert trie.search("b..n..") == False # "b..n.." doesn't match any word
    assert trie.search("..") == False  # ".." doesn't match anything because it's too short


def test_find_words_on_board_basic():
    board = [['b', 'y', 's'], ['r', 't', 'e'], ['a', 'i', 'n']]
    words = ['byte', 'bytes', 'rat', 'rain', 'trait', 'train']

    result = find_all_words_on_a_board(board, words)
    # result = solver.find()

    assert result == ['byte', 'bytes', 'rain', 'train']

    
