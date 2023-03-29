class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        
        '''
        satisfaction = [-1,-8,0,5,-9]
        
        algo:
        1. sort dished lowest -> greatest
        2. Top down DP looking ofr max satisfaction (dishIndex, timeMult)
            max(choosing this dish, skipping this dish)
            
        Time+ Space Complexity: O(nxn) where n is number of dishes
        
        '''
        satisfaction.sort()
        @cache
        def dp(dishIndex, timeMult):
            if dishIndex == len(satisfaction):
                return 0
            # choose to pick or not pick
            return max((satisfaction[dishIndex] * timeMult) + dp(dishIndex+1, timeMult+1),
                      dp(dishIndex+1, timeMult))
            
        
        return dp(0, 1)
        