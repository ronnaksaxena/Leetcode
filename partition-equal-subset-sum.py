class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        
        if total%2:
            return False
        
        target = total // 2
        n = len(nums)
        
        DP = [[False for _ in range(target+1)] for _ in range(n+1)]
        DP[0][0] = True
        
        for i in range(1,len(DP)):
            for j in range(len(DP[0])):
                if nums[i-1] <= j:
                    DP[i][j] = max(DP[i-1][j],DP[i-1][j-nums[i-1]])
                else:
                    DP[i][j] = DP[i-1][j]
                    
        return DP[-1][-1]
