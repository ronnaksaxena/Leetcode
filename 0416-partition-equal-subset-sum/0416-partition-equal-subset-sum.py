class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        Check if theres a sum that == sum(nums) // 2
        
        edge case: sum(nums) if odd
        
        [1,5,11,5] ==> sum is 22, half is 11
        
        DP[i][j] = canPartitions elements nums[:i-1] to == j
        
        if nums[i-1] >= j:
            DP[i][j] = DP[i-1][j-nums[i-1]]
        else:
            DP[i][j] = DP[i-1][j]
            
        return DP[-1][-1]
            
        
        0 1 2 3 4 5 6 7 8 9 10 11
      0 T
      1 F T F F F F F F
      5 F F F F F T 
      11                       T
      5
        
        
        '''
        total = sum(nums)
        # Odd sum
        if total%2 == 1:
            return False
        half = total // 2
        # Element equals half
        if any(x == half for x in nums):
            return True
        
        DP = [[False for _ in range(half+1)] for _ in range(len(nums)+1)]
        # Base Case
        DP[0][0] = True
        for i in range(1, len(DP)):
            for j in range(1, len(DP[0])):
                if j >= nums[i-1]:
                    DP[i][j] = DP[i-1][j-nums[i-1]] or DP[i-1][j]
                else:
                    DP[i][j] = DP[i-1][j]
        # Final solution at bottom left
        return DP[-1][-1]
        
        
        
        
        
        
        