class Solution:
    def isGoodNum(self, N:int) -> bool:
        Narr = [d for d in str(N)]
        if ('3' in Narr) or ('4' in Narr) or ('7' in Narr):
            return False
        if ('2' not in Narr) and ('5' not in Narr) and ('6' not in Narr) and ('9' not in Narr):
            return False
        return True
    def rotatedDigits(self, N: int) -> int:
        goodNums = 0
        for i in range(N+1):
            if self.isGoodNum(i):
                goodNums += 1
        return goodNums
        
