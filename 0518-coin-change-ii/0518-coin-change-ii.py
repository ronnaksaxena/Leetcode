class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        DP = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        for r in range(len(DP)):
            DP[r][0] = 1
        for i in range(1, len(DP)):
            coin = coins[i-1]
            for am in range(1, len(DP[0])):
                if coin <= am:
                    DP[i][am] = DP[i-1][am] + (DP[i][am-coin])
                else:
                    DP[i][am] = DP[i-1][am]
                    
        return DP[-1][-1]