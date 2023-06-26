class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, holding):
            if i == len(prices):
                return 0
            if holding:
                # Can choose to either sell or keep holding
                return max(prices[i] - fee + dp(i+1, False), dp(i+1, True))
            else:
                # Can choose to either buy or keep empty hands
                return max(-prices[i] + dp(i+1, True), dp(i+1, False))
        
        return dp(0, False)