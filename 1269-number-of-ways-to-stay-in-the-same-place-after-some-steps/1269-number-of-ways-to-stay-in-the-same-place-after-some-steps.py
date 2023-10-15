class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dp(stepsLeft, pos):
            if stepsLeft == 0:
                return 1 if pos == 0 else 0
            ways = 0
            if pos > 0:
                # can go left
                ways += dp(stepsLeft-1, pos-1)
            if pos < (arrLen - 1):
                # can go right
                ways += dp(stepsLeft-1, pos+1)
            # stay
            ways += dp(stepsLeft-1, pos)
            return ways
        return dp(steps, 0)%(10**9+7)
                
        