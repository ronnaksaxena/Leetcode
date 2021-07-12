class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sArr, tArr = [], []
        
        for c in s:
            if c == '#':
                if sArr:
                    sArr.pop()
            else:
                sArr.append(c)
        
        for c in t:
            if c == '#':
                if tArr:
                    tArr.pop()
            else:
                tArr.append(c)
​
        return tArr == sArr
        
            
