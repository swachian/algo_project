class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                new_node = TrieNode()
                node.children[c] = new_node
            node = node.children[c]
        node.isword = True
        
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isword

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
        node.isword = True

    def search(self, word):
        return self._search(word, self.root)
    
    def _search(self, word, node):
        for index, c in enumerate(word):
            if c == ".":
                for child in node.children.values():
                    if self._search(word[index + 1:], child):
                        return True
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        return node.isword



class TrieNodeWord:
    def __init__(self):
        self.children = {}
        self.word = None
        
        
        
    
    
def find_all_words_on_a_board(board, words):
    root = TrieNodeWord()
    for word in words:
        node = root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNodeWord()
            node = node.children[c]
        node.word = word
    
    if not board:
        return []
    
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs_find_all_words_on_a_board(board, i, j, root, res)
    return res

def dfs_find_all_words_on_a_board(board, i, j, tw, res):
    c = board[i][j]
    if tw.word:
        res.append(tw.word)
        tw.word = None
    
    board[i][j] = '#' 
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    for dir in dirs:
        n_i, n_j = i + dir[0], j + dir[1]
        if is_valid_i_j(n_i, n_j, board) and c in tw.children:
            dfs_find_all_words_on_a_board(board, n_i, n_j, tw.children[c], res)
    board[i][j] = c
    
    
def is_valid_i_j(i, j, board):
    return 0 <= i < len(board) and 0 <= j < len(board[0])