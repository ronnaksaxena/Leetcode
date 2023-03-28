class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxProfit = 0
        
        for p in prices[1:]:
            maxProfit = max(maxProfit, p- minPrice)
            minPrice = min(minPrice, p)
            
        return maxProfit
            
        