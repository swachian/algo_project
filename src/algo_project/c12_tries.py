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
            if not node.is_in(c):
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
    
    def search(self, word):
        node = self.root
        for c in word:
            if not node.is_in(c):
                return False
            node = node.children[c]
        return node.is_word
    
    def has_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if not node.is_in(c):
                return False
            node = node.children[c]
        return True
    
class InsertAndSearchWordsWithWildcards:
    def __init__(self):
        self.root = TrieNode()
        self.is_word = False
        
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
    
    def search(self, word):
        return self.search_helper(0, self.root, word)
    
    def search_helper(self, word_index, node, word):
        for i in range(word_index, len(word)):
            c = word[i]
            if c == ".":
                for child in node.children.values():
                    if self.search_helper(i + 1, child, word):
                        return True
                return False
            elif c in node.children:
                node = node.children[c]
            else:
                return False
        return node.is_word

class TrieNodeWord:
    def __init__(self):
        self.children = {}
        self.word = None
   
def find_all_words_on_a_board(board, words):
    res = []
    # 1. Build Tries
    root = TrieNodeWord()
    for word in words:
        node = root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNodeWord()
            node = node.children[c]
        node.word = word
    # 2. Iterator every char of the board only if it is a child of tries
    m = len(board)
    n = len(board[0])
    for r in range(m):
        for c in range(n):
            if board[r][c] in root.children:
                dfs(board, r, c, root.children[board[r][c]], res)
    # 3. dfs function
    # 4. if node is a word, record it and erase it from node
    # 5. set board index to '#' temporarily to avoid re-backtrack
    # 6. def recursive calls to 4 direction only if the direction is valid
    # 7. set back c to board index
    return res

def dfs(board, r, c, node, res):
    if node.word:
        res.append(node.word)
        node.word = None
    temp = board[r][c]
    board[r][c] = '#'
    
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dir in dirs:
        n_r = r + dir[0]
        n_c = c + dir[1]
        if is_valid_r_c(board, n_r, n_c):
            if board[n_r][n_c] in node.children:
                dfs(board, n_r, n_c, node.children[board[n_r][n_c]], res)
    
    board[r][c] = temp
            
def is_valid_r_c(board, r, c):
    return r >= 0 and r < len(board) and c >=0 and c < len(board[0])