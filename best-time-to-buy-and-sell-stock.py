class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minDay = float('inf')
        
        for price in prices:
            if price - minDay > profit:
                profit = price - minDay
            
            minDay = min(minDay, price)
                
        return profit
        
