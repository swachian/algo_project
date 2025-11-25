class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
    def is_in(self, c):
        return c in self.children
         

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
    
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word
    
    def has_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
    
    
  
class InsertAndSearchWordsWithWildcards:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
    
    def search(self, word):
        return self._search(self.root, word)
    
    def _search(self, node, word):
        if not node:
            return False
        for i, c in enumerate(word):
            if c == ".":
                for child in node.children.values():
                    if self._search(child, word[i + 1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            else:
                node = node.children[c]
        return node.is_word
    
    
    
class TrieNodeWord:
    def __init__(self):
        self.children = {}
        self.word = None

   
def find_all_words_on_a_board(board, words):
    if not board:
        return []
    root = _build_word_tries(words)
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
             _dfs_find_words(board, root, i, j, res)
    return res
    
    
    
def _build_word_tries(words):
    root = TrieNodeWord()
    for word in words:
        node = root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNodeWord()
            node = node.children[c]
        node.word = word
    return root
        
def _dfs_find_words(board, node, i, j, res):
    if node.word:
        res.append(node.word)
        node.word = None
    
    temp = board[i][j]
    board[i][j] = "#"
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    for dir in dirs:
        new_i, new_j = i + dir[0], j + dir[1]
        if _is_valid_bound(new_i, new_j, len(board), len(board[0])) and board[new_i][new_j] in node.children:
            _dfs_find_words(board, node.children[board[new_i][new_j]], new_i, new_j, res)    
    
    board[i][j] = temp
    
def _is_valid_bound(i, j, m, n):
    return 0 <= i < m and 0 <= j <n