class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        
        while l < r:
            
            k = l + (r-l)//2
            timeNeeded = 0
            for p in piles:
                timeNeeded += math.ceil(p/k)
            # too slow
            if timeNeeded > h:
                l = k + 1
            else:
                r = k
                
        return l
                
                
            
                
            
        