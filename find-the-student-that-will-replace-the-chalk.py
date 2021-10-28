class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        i = 0
        
        k %= sum(chalk)
        
        while chalk[i] <= k:
            
            k -= chalk[i]
            i = (i+1)%len(chalk)
            
        return i
