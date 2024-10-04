class Node:
    def __init__(self):
        self.isEOW = False #flag to check if node is end of word searching for
        self.children = {} # points to next nodes (next char: node)

class Trie:

    def __init__(self):
        self.root = Node()
        
    #Time: O(m) : m is len of key
    #Space: O(m) : if word doesn't exist have to create it
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            #char in trie already
            if c in cur.children:
                cur = cur.children[c]
            #need to append node of char value
            else:
                cur.children[c] = Node()
                cur = cur.children[c]
            
        #mark last node's flag true
        cur.isEOW = True
            
                
    #Time: O(m) : m is len of key
    #Space: O(1) : not creating anything
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            #char in prefic branch
            if c in cur.children:
                cur = cur.children[c]
            #char not in branch
            else:
                return False
        
        #check if it is end of the word
        return cur.isEOW
        
    #Time: O(m) : m is len of key
    #Space: O(1) : not creating anything
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            #char in prefic branch
            if c in cur.children:
                cur = cur.children[c]
            #char not in branch
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''
            r
            



'''