class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            # rate is the median in this case
            rate = l + (r-l)//2
            hoursNeeded = 0
            for p in piles:
                hoursNeeded += math.ceil(p/rate)
            if hoursNeeded > h:
                l = rate + 1
            else:
                r = rate
        
        return l
