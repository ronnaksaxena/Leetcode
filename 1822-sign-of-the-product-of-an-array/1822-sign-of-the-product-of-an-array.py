class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        
        for n in nums:
            prod *= n
            if prod == 0:
                return 0
            
        return 1 if prod > 0 else -1
        