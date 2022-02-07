class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Sort both the strings
        sorted_s = sorted(s)
        sorted_t = sorted(t)
​
        # Character by character comparison
        i = 0
        while i < len(s):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
            i += 1
​
        return sorted_t[i]
        
        
        '''
s       a   b   c   d
        i
        
t       a   b   c   d   e        
        
        
        '''
