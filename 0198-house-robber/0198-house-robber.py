class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        DP = [0 for _ in range(n+1)]
        DP[0], DP[1] = 0, nums[0]
        
        for i in range(1, len(DP)):
            DP[i] = max(DP[i-2] + nums[i-1], DP[i-1])
        
        return DP[-1]
        