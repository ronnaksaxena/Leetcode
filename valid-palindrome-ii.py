class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(l, r, s):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
                
            return True
        
        if isValid(0,len(s)-1, s):
            return True
        
        l, r = 0, len(s)-1
        
        while l < r:
            if s[l] != s[r]:
                return isValid(l+1, r, s) or isValid(l, r-1,s)
            
            l += 1
            r -= 1
            
        return True
