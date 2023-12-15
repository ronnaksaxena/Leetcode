class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        @cache
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return freq[1]
            else:
                return max(freq[i] * i + dp(i-2), dp(i-1))
        return dp(max(nums))
        