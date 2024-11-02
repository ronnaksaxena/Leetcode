class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0 for _ in range(n+1)]

        for i in range(2, len(dp)):
            option1 = dp[i-1] + cost[i-1]
            option2 = dp[i-2] + cost[i-2]
            dp[i] = min(option1, option2)

        return dp[n]