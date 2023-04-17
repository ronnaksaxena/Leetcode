class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        # Base cases
        # Empty string is 1 combo
        dp[0] = 1
        # First digit has 1 combo unless leading zero
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, len(dp)):
            # No leading 0
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            # There was a double formed, needs to be >= 10 for no leading 0
            twoDig = int(s[i-2:i])
            if 10 <= twoDig <= 26:
                dp[i] += dp[i-2]

        return dp[-1]
                