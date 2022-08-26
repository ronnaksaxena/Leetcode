class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top down approach
        memo = {}
        def dp(i):
            # Base case
            if i <= 1:
                return 0
            if i not in memo:
                # Compute previous 
                down_one = cost[i-1] + dp(i-1)
                down_two = cost[i-2] + dp(i-2)
                memo[i] = min(down_one, down_two)
            return memo[i]
        
        return dp(len(cost))
