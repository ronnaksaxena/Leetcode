class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        minPrice = prices[0]
        bestProfit = 0
        for p in prices[1:]:
            bestProfit = max(bestProfit, p - minPrice)
            minPrice = min(minPrice, p)
            
        return bestProfit
            