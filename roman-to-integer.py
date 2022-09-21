class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        stack = []
        res = 0
        
        for c in s:
            # Found non exact number
            if stack and vals[stack[-1]] < vals[c]:
                res -= vals[stack[-1]]
                res += vals[c]-vals[stack[-1]]
            else:
                res += vals[c]
            
            stack.append(c)
            
        return res
                
        
