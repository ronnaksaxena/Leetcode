class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNext(n):
            digits = [int(x)** 2 for x in str(n)]
            return sum(digits)
        
        seen = set()
        while n not in seen and n != 1:
            seen.add(n)
            n = getNext(n)
            
        return n == 1
        
