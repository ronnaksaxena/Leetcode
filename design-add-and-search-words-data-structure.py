class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        
​
        
class WordDictionary:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
​
    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True
        
        return
        
        
​
    def search(self, word: str) -> bool:
        cur = [self.root]
        for i, c in enumerate(word):
            newcur = []
            for node in cur:
                for ck, cv in node.children.items():
                    if c == '.' or c == ck:
                        if i == len(word) - 1 and cv.isEndOfWord:
                            return True
                        newcur.append(cv)
            cur = newcur
        return False
                    
                    
                    
        
        
​
​
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
