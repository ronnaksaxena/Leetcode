class Solution:
    def calculate(self, s: str) -> int:
        # Stack would have at most 2 parts
        inner = 0
        outer = 0
        ans = 0
        prevSign = '+'
        s = s.replace(' ', '') # Remove whitestpace
        
        for i in range(len(s)):
            
            if s[i].isnumeric():
                inner = inner*10 + int(s[i])
                
            # if not elif becuase last char could be num
            if s[i] in '+-/*' or i == len(s)-1:
                if prevSign == '+':
                    # Add last term to result
                    ans += outer
                    outer = inner
                elif prevSign == '-':
                    ans += outer
                    outer = -inner
                elif prevSign == '*':
                    outer *= inner
                elif prevSign == '/':
                    outer = int(outer / inner)
                inner, prevSign = 0, s[i]
                
        return ans + outer
                    
            