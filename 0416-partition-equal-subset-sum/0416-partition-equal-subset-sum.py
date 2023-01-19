class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        #if total is odd cannot create partition that equals it
        if total % 2 == 1:
            return False
        
        target = sum(nums) // 2 #val we want to see if we can sum towards

        n = len(nums)
        
        DP = [[False for _ in range(target+1)] for _ in range(n+1)]
        #base case: empty nums sums to 0
        DP[0][0] = True
        
        for i in range(1, len(DP)):
            for j in range(1, len(DP[0])):
                
                #can pick number? for cur target
                if j >= nums[i-1]:
                    #choose to either pick or not pick
                    DP[i][j] = DP[i-1][j] or DP[i-1][j-nums[i-1]]
                    
                else:
                    DP[i][j] = DP[i-1][j]
                    

        return DP[-1][-1]