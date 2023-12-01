class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        '''
        word1 = ["ab", "c"]
                  j
                  i
        word2 = ["a", "bc"]
                  j
                  i
        
        While i1 < len(word1) and i2 < len(word2):
            - check if they all match word1[i][j] == word2[i][j]
            - update points j += 1
                - if j > len(word[i]): i += 1, j = 0
        
        return i1 == len(word1) and i2 == len(word2)
        '''
        
        i1, j1 = 0, 0 # i is outer, j is inner
        i2, j2 = 0, 0
        
        while i1 < len(word1) and i2 < len(word2):
            if word1[i1][j1] != word2[i2][j2]:
                return False
            j1 += 1
            if j1 == len(word1[i1]):
                i1 += 1
                j1 = 0
            j2 += 1
            if j2 == len(word2[i2]):
                i2 += 1
                j2 = 0
                
        return i1 == len(word1) and i2 == len(word2)
        
        
        
        
        
        
        