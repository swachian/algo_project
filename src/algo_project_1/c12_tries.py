class TrieNode:
    # Trie用于记录一串可能的链，链之间的连接使用hash实现，每个node除了children,还有记录一个完整的word,或者用一个boolean表示这是否是一个word的终结
    # 插入的时候就是沿着hash,一个一个的插入进去，没有就新建。查找或者索引的时候也是一个一个往下找，但需要注意是否要判断是否是结尾
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
    # 这个东西最大的注意点在于search的时候，如果碰到.，那么就要发动当前所有的children去搜寻下一个字串，有一个搜索到就返回True
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
    # 首先把输入的words都编成tries,便于后面查找
    # 对于board,要用m*n的方式，从每一个入口递归遍历寻找匹配的对象，所以res是作为参数传入
    # 遍历时， 4. if node is a word, record it and erase it from node
    # 5. set board index to '#' temporarily to avoid re-backtrack
    # 6. def recursive calls to 4 direction only if the direction is valid
    # 7. set back c to board 
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