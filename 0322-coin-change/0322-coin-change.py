class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        coins = [1,2,5], amount = 11
        
        BASE CASE: amount = 0, answer = 0
        
        if coin <= amount:
            DP[coin][amount] = min(DP[coin-1][amount], DP[coin][amount-coin]+1)
            
        PSUEDOCODE:
        init DP arr [[amount+1] coints + 1] => defaul values of inf
        for r in len(DP):
            DP[r][0] = 0
        loop coin through DP rows:
            loop am through DP coin:
                if coin <= amount:
                    DP[coin][amount] = min(DP[coin-1][amount], DP[coin][amount-coin]+1)
                else:
                    DP[coin][amount] = DP[coin-1][amount]
        return DP[-1][-1] if answer exits
        '''
        
        DP = [[float('inf') for _ in range(amount+1)] for _ in range(len(coins)+1)]
        for r in range(len(DP)):
            DP[r][0] = 0
        for i in range(1, len(DP)):
            coin = coins[i-1]
            for am in range(1, len(DP[0])):
                if coin <= am:
                    DP[i][am] = min(DP[i-1][am], DP[i][am-coin] + 1)
                else:
                    DP[i][am] = DP[i-1][am]
                    
        return DP[-1][-1] if DP[-1][-1] != float('inf') else -1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        