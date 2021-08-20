class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        S = (total+target)//2
        
        if (total+target)%2 == 1 or (abs(target) > total):
            return 0
​
        
        DP = [0 for _ in range(S+1)]
        DP[0] = 1
        
        for num in nums:
            for j in range(S,num-1,-1):
                DP[j] += DP[j-num]
                    
        
        return DP[-1]
