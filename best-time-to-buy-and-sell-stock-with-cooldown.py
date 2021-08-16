class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        n = len(prices)
        noStock = [0 for _ in range(n)]
        inHand = [0 for _ in range(n)]
        sold = [0 for _ in range(n)]
        
        noStock[0], sold[0] = 0, 0
        inHand[0] = 0 - prices[0]
        
        for i in range(1,n):
            noStock[i] = max(noStock[i-1],sold[i-1])
            inHand[i] = max(inHand[i-1],noStock[i-1]-prices[i])
            sold[i] = prices[i] + inHand[i-1]
            
        return max(noStock[-1],sold[-1])
