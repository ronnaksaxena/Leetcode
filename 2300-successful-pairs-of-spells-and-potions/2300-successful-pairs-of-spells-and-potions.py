class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        output = [0 for _ in range(len(spells))]
        
        for i, s in enumerate(spells):
            # Bsearch to find max number of successful pairs
            l, r = 0, len(potions)
            while l < r:
                m = l + (r-l)//2
                if (s * potions[m]) < success:
                    l = m + 1
                else:
                    r = m
            output[i] = len(potions)-l
        
        return output
            
        