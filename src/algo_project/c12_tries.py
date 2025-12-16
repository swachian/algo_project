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
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isword = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        return node.isword
    
    def has_prefix(self, prefx):
        node = self.root
        for c in prefx:
            if c not in node.children:
                return False
            else:
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
    
class TrieWord:
    def __init__(self):
        self.root = TrieNodeWord()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNodeWord()
            node = node.children[c]
        node.word = word

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        return node.word != None
    

    
def find_all_words_on_a_board(board, words):
    if not board:
        return []
    trie = TrieWord()
    for word in words:
        trie.insert(word)
        
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in trie.root.children:
                dfs_find_all_words_on_a_board(board, trie.root.children[board[i][j]], i, j, res)
    return res
        
def dfs_find_all_words_on_a_board(board, node, i, j, res):
    c = board[i][j]
    if node.word:
        res.append(node.word)
        node.word = None
        # return
    board[i][j] = '#'
    
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dir in dirs:
        next_i, next_j = i + dir[0], j + dir[1]
        if is_in_bound(next_i, next_j, board) and board[next_i][next_j] in node.children:
            dfs_find_all_words_on_a_board(board, node.children[board[next_i][next_j]], next_i, next_j, res)
    
    board[i][j] = c
    
def is_in_bound(i, j, board):
    return 0 <= i < len(board) and 0 <= j < len(board[0])