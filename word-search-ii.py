class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            
        cur.isEnd = True
​
class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        
        for word in words:
            root.addWord(word)
            
        output, visited = set(), set()
        m, n = len(board), len(board[0]) #rows, cols
        
        def dfs(r, c, node, word):
            if (0 > r or r >= m or c < 0 or c >= n or (r,c) in visited or board[r][c] not in node.children):
                return
