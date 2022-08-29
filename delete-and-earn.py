class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        memo = {}
        def dp(i):
            nonlocal freq
            nonlocal memo
            if i == 0:
                return 0
            if i == 1:
                return freq[1]
            if i not in memo:
                memo[i] = max(freq[i] * i + dp(i-2), dp(i-1))
            return memo[i]
        
        return dp(max(nums))
