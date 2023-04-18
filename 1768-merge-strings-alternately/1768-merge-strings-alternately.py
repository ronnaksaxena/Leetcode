class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def merge(w1, w2, turn1):
            if not w1 and not w2:
                return ''
            elif not w1:
                return w2
            elif not w2:
                return w1
            elif turn1:
                return w1[0] + merge(w1[1:], w2, not turn1)
            else:
                return w2[0] + merge(w1, w2[1:], not turn1)
            
        
        return merge(word1, word2, True)
        