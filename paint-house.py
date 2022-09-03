class Solution:
    # red, blue, green
    def minCost(self, costs: List[List[int]]) -> int:
        
        dp = [0, 0, 0]
        
        for i in range(len(costs)):
            # Red
            dp0 = costs[i][0] + min(dp[1], dp[2])
            # Blue
            dp1 = costs[i][1] + min(dp[0], dp[2])
            # Green
            dp2 = costs[i][2] + min(dp[1], dp[0])
            
            dp = [dp0, dp1, dp2]
            
        return min(dp)
            
            
                        
