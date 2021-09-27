class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        opens, closes = 0, 0
        
        for c in s:
            if c == '(':
                opens += 1
            else:
                if opens == 0:
                    closes += 1
                else:
                    opens -= 1
                    
        return opens + closes
