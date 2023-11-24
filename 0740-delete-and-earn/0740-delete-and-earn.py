class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        maxNum = max(nums)
        @cache
        def dp(i):
            if i <= 1:
                return cnt.get(i, 0)
            return max(dp(i-1), dp(i-2) + (cnt[i] * i))
        return dp(maxNum)
        