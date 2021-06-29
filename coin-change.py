class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        coins.sort()
        
        for i in range(len(dp)):
            for coin in coins:
                if coin > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i-coin])
                        
        return dp[-1] if dp[-1] != float('inf') else -1
                
