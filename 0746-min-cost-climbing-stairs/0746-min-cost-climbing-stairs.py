class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        # Treat step i + 1 as top floor or goal state
        DP = [0 for _ in range(len(cost)+1)]
        
        DP[0] = 0
        DP[1] = 0
        
        for step in range(2, len(DP)):
            DP[step] = min(cost[step-1] + DP[step-1], cost[step-2] + DP[step-2])
        return DP[-1]
        