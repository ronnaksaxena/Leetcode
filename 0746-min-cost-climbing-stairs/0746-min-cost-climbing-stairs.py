class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @lru_cache
        def dp(step):
            if step <= 1:
                return cost[0] if step == 0 else cost[1]
            
            return cost[step] + min(dp(step-1), dp(step-2))

        return min(dp(len(cost)-1), dp(len(cost)-2))
        
        '''
        [10,15,20]
               i

        '''