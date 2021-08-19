class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, len(dp)):
            
            if s[i-1] != '0':
                dp[i] = dp[i-1]
                
            twoDig = int(s[i-2:i])
            if 10 <= twoDig <= 26:
                dp[i] += dp[i-2]
​
        return dp[-1]
                
