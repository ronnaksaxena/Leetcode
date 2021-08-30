class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        
        
        return max(self.robHouse(nums[1:]), self.robHouse(nums[:-1]))
    
    def robHouse(self, nums):
            n = len(nums)
            
            DP = [0 for _ in range(n+1)]
            DP[0] = 0
            DP[1] = nums[0]
            
            for i in range(2, len(DP)):
                
                DP[i] = max(DP[i-1], DP[i-2] + nums[i-1])
                
            return DP[-1]
    
    
