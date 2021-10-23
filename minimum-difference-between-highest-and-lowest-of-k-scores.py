class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        nums.sort()
        minDif = float('inf')
        l, r = 0, k-1
        
        while r < len(nums):
            minDif = min(minDif, nums[r]-nums[l])
            l += 1
            r += 1
            
        return minDif
        
