class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        
        DP = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        
        for row in range(len(DP)):
            DP[row][0] = 1
            
​
        
        for i in range(1, len(DP)):
            for j in range(len(DP[0])):
                if coins[i-1] <= j:
                    DP[i][j] = DP[i][j-coins[i-1]] + DP[i-1][j]
                else:
                    DP[i][j] = DP[i-1][j]
                    
                    
        return DP[-1][-1]
