class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        DP = [0 for _ in range(len(nums) + 1)]
        DP[-1], DP[-2] = 0, nums[-1]
        for i in range(len(nums)-2, -1, -1):
            
            DP[i] = max(DP[i+1], DP[i+2]+nums[i])
        return DP[0]
        
