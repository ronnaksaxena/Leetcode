class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []
        
        sArr, pArr = [0] * 26, [0] * 26
        for c in p:
            pArr[ord(c)-ord('a')] += 1
            
        output = []
        
        for i in range(len(s)):
            sArr[ord(s[i])-ord('a')] += 1
            
                
            if i >= len(p):
                sArr[ord(s[i-len(p)])-ord('a')] -= 1
                
            if sArr == pArr:
                output.append(i-len(p)+1)
                
        return output
        
        
'''
s   cbaebabacd
     l
       r
      
    {a, b, r}
​
​
