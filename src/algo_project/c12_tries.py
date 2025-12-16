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